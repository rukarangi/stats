import csv
import os

files = {"CSVs/boy2009": 31, 
        "CSVs/girl2009": 31, 
        "CSVs/boy2011": 27, 
        "CSVs/girl2011": 27,
        "CSVs/boy2013": 41,
        "CSVs/girl2013": 41,
        "CSVs/boy2015": 34,
        "CSVs/girl2015": 34,
        "CSVs/boy2017": 31,
        "CSVs/girl2017": 31}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mathPart(gender20xx, test, save, name):
    sortedL = sortedL[1:]
    sortedL = sorted(gender20xx)
    lengthL = len(sortedL)
    floatSort = []
    val = 0
    
    nullvals = 0
    zerovals = 0
    for pos in xrange(0, lengthL):
        if sortedL[pos] == '':
            nullvals += 1
        if sortedL[pos] == '0':
            zerovals += 1

    for pos in xrange(0, nullvals):
        sortedL.remove('')

    for pos in xrange(0, zerovals):
        sortedL.remove('0')
    if test:
        print(zerovals)
        print(nullvals)
        print(sortedL)

    for x in sortedL:
        floatSort.append(float(x))
        
    length = len(sortedL)

    evenness = testEven(len(floatSort))
    lowerHalf = floatSort[0:int(length/2)] if evenness == False else floatSort[0:int(length/2-1)]
    upperHalf = floatSort[int(length/2+1):-1] if evenness == False else floatSort[int(length/2):-1]

    lowerQ = workMedian(lowerHalf)
    upperQ = workMedian(upperHalf)
    median = workMedian(floatSort)

    range = floatSort[-1] - floatSort[0]
    
    total = 0.00
    loopy = buildList(length)
    for y in loopy:
        currentVal = floatSort[y]
        #print(currentVal)
        total += currentVal
    mean = total/length

    output_vals = {}

    if test:
        print("List: ")
        print(floatSort)
    print("Length: " + str(length))
    output_vals["Length"] = length
    print("Total: " + str(total))
    output_vals["Total"] = total
    print("Range: " + str(range))
    output_vals["Range"] = range
    print("Mean: " + str(mean))
    output_vals["Mean"] = mean
    print("Median: " + str(median))
    output_vals["Median"] = median 
    print("Lowest: " + str(floatSort[0]))
    output_vals["Lowest"] = floatSort[0]
    print("Lower Quartile: " + str(lowerQ))
    output_vals["LQ"] = lowerQ
    print("Upper Quartile: " + str(upperQ))
    output_vals["UQ"] = upperQ
    print("Highest: " + str(floatSort[-1]))
    output_vals["Highest"] = floatSort[-1]
    print("Number of people with no answer:" + str(zerovals + nullvals))
    output_vals["No. NA"] = zerovals + nullvals

    print("")
    print(output_vals)
    print('=' * 40)

    if save:
        with open('summary.txt', 'a') as f:
            f.write('\n')
            f.write('\n')
            f.write(name + ": \n")
            for key, val in output_vals.items():
                f.write("\n" + key + ": " + str(val))
            f.write("\n" + "="*40)
            f.close()

def workMedian(floatSort):
    length = len(floatSort)
    even = testEven(length)
    return floatSort[int(length/2)] if even == False else (
        floatSort[int((length/2)-1)]
         + floatSort[int(length/2)])/2

def testEven(inty):
    if inty % 2 == 0:
        return True
    else:
        return False

def buildList(length):
	i = 0
	infinity = []
	while i < length:
		infinity.append(i)
		i = i + 1
	return infinity

def runValues(fileName, valueList, pos, name):
    with open(fileName) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            valueList.append(row[pos])
    input0 = raw_input("Please enter True or False if you want a test: ")
    if input0 == "True":
        test = True
    else:
        test = False
    save = True
    mathPart(valueList, test, save, name)
            
def whole(name, empty, pos):
    clear()
    print(name)
    print("")
    file = name + ".csv"
    runValues(file, empty, pos, name)
    print("")

def statSum(files):
    input1 = raw_input("Whould you like to clear the file?: [y/n] ")
    with open('summary.txt', 'w') as f:
        f.write("")
        f.close()
    for file, pos in files.items():
	    whole(file, [], pos)

if __name__ == '__main__':    
    statSum(files)