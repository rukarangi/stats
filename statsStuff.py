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


def mathPart(gender20xx, test, save, name):
    sortedL = sorted(gender20xx)
    sortedL = sortedL[:-1]

    nullvals = len([v for v in sortedL if v == ''])
    zerovals = len([v for v in sortedL if v == '0'])

    sortedL = [ v for v in sortedL if v != '' and v != '0']

    if test:
        print(zerovals)
        print(nullvals)
        print(sortedL)

    floatSort = [ float(x) for x in sortedL ]
        
    length = len(sortedL)

    evenness = testEven(len(floatSort))
    lowerHalf = floatSort[0:int(length/2)]     if not evenness else floatSort[0:int(length/2-1)]
    upperHalf = floatSort[int(length/2+1):-1]  if not evenness else floatSort[int(length/2):-1]

    if test:
        print("List: ")
        print(floatSort)

    output_vals = {
        "Length"    : length,
        "Total"     : sum(floatSort),
        "Range"     : floatSort[-1] - floatSort[0],
        "Mean"      : sum(floatSort)/length,
        "Median"    : workMedian(floatSort), 
        "Lowest"    : floatSort[0],
        "LQ"        : workMedian(lowerHalf),
        "UQ"        : workMedian(upperHalf),
        "Highest"   : floatSort[-1],
        "No. NA"    : zerovals + nullvals
        }

    order = ["Length", "Total", "Range", "Mean", "Median", "Lowest", "LQ", "UQ", "Highest", "No. NA"]

    for key in order:
        print(key + ": " + str(output_vals[key]))

    print("")
    print(output_vals)
    print('=' * 40)

    if save:
        with open('summary.txt', 'a') as f:
            f.write('\n')
            f.write('\n')
            f.write(name + ": \n")
            for key in order:
                f.write("\n" + key + ": " + str(output_vals[key]))
            f.write("\n" + "="*40)
            f.close()

def workMedian(floatSort):
    length = len(floatSort)
    even = testEven(length)
    return floatSort[int(length/2)] if even == False else (
        floatSort[int((length/2)-1)]
         + floatSort[int(length/2)])/2

def testEven(inty):
    return inty % 2 == 0


def main(files):
    input1 = raw_input("Whould you like to clear the file?: [y/n] ")
    
    if input1 == 'y':
        with open('summary.txt', 'w') as f:
            f.write("")
            f.close()
    
    for name, pos in files.items():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(name)
        print("")   
        file = name + ".csv"
        valueList = []
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                valueList.append(row[pos])
        input0 = raw_input("Please enter True or False if you want a test: ")
        test = input0 == "True"
        save = True
        mathPart(valueList, test, save, name)
        print("")

if __name__ == '__main__':    
    main(files)

