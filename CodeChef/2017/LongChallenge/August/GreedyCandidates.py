def solution(candidates, companies, qual, offeredSalary, maxJobOffers, minSalary):
    nEmployedByCompany = [0] * len(companies)
    nCandidateEmployed = 0
    totalSalaries = 0
    for candidate in candidates:
        maxOfferedCandidate = 0
        candidateCompany = None
        for company in companies:
            if qual[candidate][company] == '1':
                if maxOfferedCandidate < offeredSalary[company] and \
                    offeredSalary[company] > minSalary[candidate] and \
                        nEmployedByCompany[company] < maxJobOffers[company]:
                    maxOfferedCandidate = offeredSalary[company]
                    candidateCompany = company
        if candidateCompany is not None:
            nEmployedByCompany[candidateCompany] += 1
            nCandidateEmployed += 1
            totalSalaries += maxOfferedCandidate
    companiesWithNoCandidate = 0
    for nCompany in nEmployedByCompany:
        if nCompany == 0:
            companiesWithNoCandidate += 1
    return nCandidateEmployed, totalSalaries, companiesWithNoCandidate


def func(s):
    return int(s)-1

T = input()
for _ in xrange(T):
    N, M = map(int, raw_input().split())
    minSalary = map(int, raw_input().split())
    offeredSalary = [0] * M
    maxJobOffers = [0] * M
    for m in xrange(M):
        offeredSalary[m], maxJobOffers[m] = map(int, raw_input().split())
    qual = [[] for i in xrange(N)]
    for i in xrange(N):
        qual[i] = raw_input()

    print '%d %d %d'%(solution(range(N), range(M), qual, offeredSalary, maxJobOffers, minSalary))
