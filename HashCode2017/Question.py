
V,E,R,C,X = map(int,raw_input().split())

cacheServerSizes = [X for i in xrange(C)] #cacheServer[0] = size
#print cacheServerSizes
cacheServerVideos = [set() for i in xrange(C)] #cacheServer[0] = (1,2) - server 0 has video 1 and 2

Endpoints = [[] for i in xrange(E)] #Endpoint[0]=[] - currently has no cacheservers connected - we will sort this when ready

Requests = [[] for i in xrange(R)] #Requests - sort by number of requests - Request[0]=(video,endpoint,number)

VideosSizes = [0]*V

VideoSizes = map(int,raw_input().split())
#print "Video Sizes",VideoSizes
for e in xrange(E):
    DatacenterLatency,K = map(int,raw_input().split())
    for k in xrange(K):
        cacheServer,latency = map(int,raw_input().split())
        Endpoints[e].append((cacheServer,latency))
    Endpoints[e].append((-1,DatacenterLatency))

for r in xrange(R):
    #rv,ro,rn = map(int,raw_input().split())
    Requests[r] = map(int,raw_input().split())


def sortByCacheIn(Endpoint):
    #Every endpoint has list of cacheServer and latency.. want to sort based on latency
    def getLatency(ServerAndLatency):
        server,latency = ServerAndLatency
        return latency 
    return sorted(Endpoint, key=getLatency)

for e in xrange(E):
    Endpoints[e]= sortByCacheIn(Endpoints[e])

def sortRequestByNumber(Requests):
    def getNumber(request):
        rv,re,rn = request
        return rn
    return sorted(Requests,key = getNumber,reverse=True)
def putVideoInCache(endpoint,video):
    "Check the endpoint in order.. look for the nearest cache that has space"
    "Add the video to the cacheServerVideos and reduce cacheSize"
    #print "Endpoint",endpoint,video,Endpoints[endpoint],VideoSizes,cacheServerSizes
    for cacheAndlatency in Endpoints[endpoint]:
        cache,latency = cacheAndlatency
        if cacheServerSizes[cache]>=VideoSizes[video] and video not in cacheServerVideos[cache]:
            cacheServerSizes[cache]-=VideoSizes[video]
            cacheServerVideos[cache].add(video)
            break
            #print "here"
    else:
        pass
        #print ("Stored in Datacenter not cache")



Requests = sortRequestByNumber(Requests)
for request in Requests:
    video,endpoint,nrequest = request
    putVideoInCache(endpoint,video)


#Result

#Need to find the number of Cache Servers we used
#Then the video stored in each cache
CacheUsed = 0
for cache in cacheServerVideos:
    if cache !=  set():
        CacheUsed+=1
print CacheUsed
for cache,videos in enumerate(cacheServerVideos):
    if videos != set():
        print cache,
        for video in videos:
            print video,
        print
        
#print Endpoints,Requests
#print VideoSizes,cacheServerSizes,cacheServerVideos
def getServer(video,endpoint):
    for cache,videos in enumerate(cacheServerVideos):
        if video in videos:
            return Endpoints[cache][-1][1]
    else:
        return Endpoints[endpoint][-1][1]
score = 0
for request in Requests:
    video,endpoint,nrequest = request
    score+=(Endpoints[endpoint][-1][1]-getServer(video,endpoint))*nrequest

