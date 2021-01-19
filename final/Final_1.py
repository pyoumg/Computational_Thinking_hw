def makeSubjectTbl(filename):

    subjTable = {}

    input_file = open(filename, "r")

    for line in input_file:

        row = line.split()

        subjects = row[1:]

        for subj in subjects:

            subj = subj.lower()

            if not subj in subjTable:

                subjTable[subj] = [row[0]]

            else:

                subjTable[subj].append(row[0])

    input_file.close()

    return subjTable


# main

subjectTbl = makeSubjectTbl("timeTable.txt")

for key, value in subjectTbl.items():

    print(key, "-", value)
