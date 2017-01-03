def maxPopulation(birth,death):
    "take a list with birth Years (integers) and death Years and return the year with max population"
    MinYear = min(birth)
    MaxYear = max(death)

    #Population for each year
    Population = [0]*(MaxYear-MinYear+2)

    #had to do this, since a year can appear multiple times. BirthYears has the number of people born in that year
    BirthYears= [0]*(MaxYear-MinYear+2)
    for year in birth:
        BirthYears[year-MinYear]+=1
    #DeathYears has the number of people that died in that year
    DeathYears= [0]*(MaxYear-MinYear+2)
    for year in death:
        DeathYears[year-MinYear+1]+=1 #if we follow Efe's assumption, year shifted by 1
    
    #Population increase is simply
    Population[0]=BirthYears[0]-DeathYears[0]
    for i in xrange(1,len(Population)):
        #Population increase is simply
        Population[i]= Population[i-1]+(BirthYears[i]-DeathYears[i])
    #print Population
    MaxPopulation = max(Population)
    MaxYears = [] 
    
    for i in xrange(len(Population)):
        if Population[i]==MaxPopulation:
            MaxYears.append(MinYear+i)
    return MaxYears

print maxPopulation([18, 0, 10, 4, 16, 2, 16],[30, 12, 22, 19, 28, 20, 28])