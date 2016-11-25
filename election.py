import json
import heapq
from tabulate import tabulate

with open('results.json') as data_file:    
    data = json.load(data_file)

mostHillary = []
mostTrump = []
mostJohnson = []
mostStein = []
mostThirdParty = []
leastTrump = []
leastHillary = []

resultsTuples = []

for i in range(1,51):
	stateName = data[i]['state_slug']
	counties = data[i]['counties']
	for county in counties:
		countyName = county['name']
		countyResults = county['results']
		hillaryVotes = countyResults['clintonh']
		trumpVotes = countyResults['trumpd']
		johnsonVotes = countyResults['johnsong']
		# Lol she must have had 0 votes in some counties
		if 'steinj' in countyResults:
			steinVotes = countyResults['steinj']
		else: 
			steinVotes = 0
		totalVotes = float(hillaryVotes + trumpVotes + johnsonVotes + steinVotes)
		hillaryPercent = hillaryVotes / totalVotes
		trumpPercent = trumpVotes / totalVotes
		johnsonPercent = johnsonVotes / totalVotes
		steinPercent = steinVotes / totalVotes
		resultsTuple = (stateName, countyName, hillaryPercent, trumpPercent, johnsonPercent, steinPercent)
		#Change this to set a minimum number of votes in the county for ranking
		minVotes = 25000
		if totalVotes > minVotes:
			resultsTuples.append(resultsTuple)

hillarySorted = sorted(resultsTuples, key=lambda x: x[2])
trumpSorted = sorted(resultsTuples, key=lambda x: x[3])
johnsonSorted = sorted(resultsTuples, key=lambda x: x[4])
steinSorted = sorted(resultsTuples, key=lambda x: x[5])
print '\n\nOnly considering counties with at least ' + str(minVotes) + ' votes'
print '\n\n10 Most Democratic'
printTuplesList = []
for i in range(0, 10):
	tup = hillarySorted[len(hillarySorted) - i - 1]
	printTup = [tup[1], tup[0], tup[2]]
	printTuplesList.append(printTup)
print tabulate(printTuplesList)

print '\n\n10 Least Democratic'
printTuplesList = []
for i in range(0, 10):
	tup = hillarySorted[i]
	printTup = [tup[1], tup[0], tup[2]]
	printTuplesList.append(printTup)
print tabulate(printTuplesList)

print '\n\n10 Most Republican'
printTuplesList = []
for i in range(0, 10):
	tup = trumpSorted[len(trumpSorted) - i - 1]
	printTup = [tup[1], tup[0], tup[3]]
	printTuplesList.append(printTup)
print tabulate(printTuplesList)

print '\n\n10 Least Republican'
printTuplesList = []
for i in range(0, 10):
	tup = trumpSorted[i]
	printTup = [tup[1], tup[0], tup[3]]
	printTuplesList.append(printTup)
print tabulate(printTuplesList)

print '\n\n10 Most Libertarian'
printTuplesList = []
for i in range(0, 10):
	tup = johnsonSorted[len(johnsonSorted) - i - 1]
	printTup = [tup[1], tup[0], tup[4]]
	printTuplesList.append(printTup)
print tabulate(printTuplesList)

print '\n\n10 Most Green'
printTuplesList = []
for i in range(0, 10):
	tup = steinSorted[len(steinSorted) - i - 1]
	printTup = [tup[1], tup[0], tup[5]]
	printTuplesList.append(printTup)
print tabulate(printTuplesList)


for i in range(len(trumpSorted)):
	tup = trumpSorted[i]
	if tup[0] == 'new-jersey' and tup[1] == 'Ocean':
		print 'Ocean county is ranked ' + str(len(trumpSorted) - i) + ' of ' + str(len(trumpSorted)) + ' counties for most Trump voters'
