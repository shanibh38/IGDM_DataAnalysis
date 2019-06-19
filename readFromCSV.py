import csv
import pandas
import math

users = {}


def readFromUsersA():
    csvFile = csv.reader(
        open(r"C:\Users\Shani Ben Haim\Desktop\demog.csv", "r"))
    for row in csvFile:
        if row[0] not in users:
            userName = {'demog': {
                "WorkerID": "", "age": "", "gender": "",  "education": "", "bonus": ""
            }, 'quiz1': {
                'minMoves': '',  'firstBox': '', 'secBox': '', 'hardme': '', 'hardthem': '', 'firstMoveRate': '',  'secondMoveRate': '', 'thirdMoveRate': '', 'forthMoveRate': '',
                'fifthMoveRate': '',   'firstBox1Rate': '', 'firstBox2Rate': '', 'firstBox3Rate': '', 'firstBox4Rate': '',
                'firstBox5Rate': '', 'firstBox6Rate': '',  'secondBox1Rate': '', 'secondBox2Rate': '', 'secondBox3Rate': '',
                'secondBox4Rate': '', 'secondBox5Rate': '', 'secondBox6Rate': '', 'resetNum': '', 'firstBoxToMove': '', 'endTime': '', 'totalMoves': '', 'histMoves': ''
            }, 'quiz2': {
                'minMoves': '',  'firstBox': '', 'secBox': '', 'firstMoveRate': '',  'secondMoveRate': '', 'thirdMoveRate': '', 'forthMoveRate': '',
                'fifthMoveRate': '',   'firstBox1Rate': '', 'firstBox2Rate': '', 'firstBox3Rate': '', 'firstBox4Rate': '',
                'firstBox5Rate': '', 'firstBox6Rate': '',  'secondBox1Rate': '', 'secondBox2Rate': '', 'secondBox3Rate': '',
                'secondBox4Rate': '', 'secondBox5Rate': '', 'secondBox6Rate': '', 'resetNum': '', 'firstBoxToMove': '', 'endTime': '', 'totalMoves': '', 'histMoves': ''
            }, 'quiz3': {
                'minMoves': '',  'firstBox': '', 'secBox': '', 'firstMoveRate': '',  'secondMoveRate': '', 'thirdMoveRate': '', 'forthMoveRate': '',
                'fifthMoveRate': '',   'firstBox1Rate': '', 'firstBox2Rate': '', 'firstBox3Rate': '', 'firstBox4Rate': '',
                'firstBox5Rate': '', 'firstBox6Rate': '',  'secondBox1Rate': '', 'secondBox2Rate': '', 'secondBox3Rate': '',
                'secondBox4Rate': '', 'secondBox5Rate': '', 'secondBox6Rate': '', 'resetNum': '', 'firstBoxToMove': '', 'endTime': '', 'totalMoves': '', 'histMoves': ''
            }, 'bq12': {
                'minMoves': '',  'firstBox': '', 'secBox': '', 'resetNum': '', 'firstBoxToMove': '', 'endTime': '', 'totalMoves': '', 'histMoves': ''
            }, 'bq23': {
                'minMoves': '',  'firstBox': '', 'secBox': '', 'resetNum': '', 'firstBoxToMove': '', 'endTime': '', 'totalMoves': '', 'histMoves': ''
            }}
            users[row[0]] = userName
        users[row[0]]['demog']['WorkerID'] = (row[1])
        users[row[0]]['demog']['age'] = (row[2])
        users[row[0]]['demog']['gender'] = (row[3])
        users[row[0]]['demog']['education'] = (row[4])
        users[row[0]]['demog']['bonus'] = (row[5])


def readFromBQ12A():
    csvFile = csv.reader(
        open(r"C:\Users\Shani Ben Haim\Desktop\bq12.csv", "r"))
    for row in csvFile:
        if row[0] in users:
            # users[row[0]] = userName
            users[row[0]]['bq12']['minMoves'] = (row[1])
            users[row[0]]['bq12']['firstBox'] = (row[2])
            users[row[0]]['bq12']['secBox'] = (row[3])
            users[row[0]]['bq12']['resetNum'] = (row[4])
            users[row[0]]['bq12']['firstBoxToMove'] = (row[5])
            users[row[0]]['bq12']['endTime'] = (row[6])
            users[row[0]]['bq12']['totalMoves'] = (row[7])
            users[row[0]]['bq12']['histMoves'] = (row[8])
        else:
            print('warning - no has user name but has rows')


def readFromBQ23A():
    csvFile = csv.reader(
        open(r"C:\Users\Shani Ben Haim\Desktop\bq23.csv", "r"))
    for row in csvFile:
        if row[0] in users:
            # users[row[0]] = userName
            users[row[0]]['bq23']['minMoves'] = (row[1])
            users[row[0]]['bq23']['firstBox'] = (row[2])
            users[row[0]]['bq23']['secBox'] = (row[3])
            users[row[0]]['bq23']['resetNum'] = (row[4])
            users[row[0]]['bq23']['firstBoxToMove'] = (row[5])
            users[row[0]]['bq23']['endTime'] = (row[6])
            users[row[0]]['bq23']['totalMoves'] = (row[7])
            users[row[0]]['bq23']['histMoves'] = (row[8])
        else:
            print('warning - no has user name but has rows')


def readFromQuiz1A():
    csvFile = csv.reader(
        open(r"C:\Users\Shani Ben Haim\Desktop\quiz1.csv", "r"))
    for row in csvFile:
        if row[0] in users:
            #    users[row[0]] = userName
            users[row[0]]['quiz1']['minMoves'] = (row[1])
            users[row[0]]['quiz1']['firstBox'] = (row[2])
            users[row[0]]['quiz1']['secBox'] = (row[3])
            users[row[0]]['quiz1']['hardme'] = (row[4])
            users[row[0]]['quiz1']['hardthem'] = (row[5])
            users[row[0]]['quiz1']['firstMoveRate'] = (row[6])
            users[row[0]]['quiz1']['secondMoveRate'] = (row[7])
            users[row[0]]['quiz1']['thirdMoveRate'] = (row[8])
            users[row[0]]['quiz1']['forthMoveRate'] = (row[9])
            users[row[0]]['quiz1']['fifthMoveRate'] = (row[10])
            users[row[0]]['quiz1']['firstBox1Rate'] = (row[11])
            users[row[0]]['quiz1']['firstBox2Rate'] = (row[12])
            users[row[0]]['quiz1']['firstBox3Rate'] = (row[13])
            users[row[0]]['quiz1']['firstBox4Rate'] = (row[14])
            users[row[0]]['quiz1']['firstBox5Rate'] = (row[15])
            users[row[0]]['quiz1']['firstBox6Rate'] = (row[16])
            users[row[0]]['quiz1']['secondBox1Rate'] = (row[17])
            users[row[0]]['quiz1']['secondBox2Rate'] = (row[18])
            users[row[0]]['quiz1']['secondBox3Rate'] = (row[19])
            users[row[0]]['quiz1']['secondBox4Rate'] = (row[20])
            users[row[0]]['quiz1']['secondBox5Rate'] = (row[21])
            users[row[0]]['quiz1']['secondBox6Rate'] = (row[22])
            users[row[0]]['quiz1']['resetNum'] = (row[23])
            users[row[0]]['quiz1']['firstBoxToMove'] = (row[24])
            users[row[0]]['quiz1']['endTime'] = (row[25])
            users[row[0]]['quiz1']['totalMoves'] = (row[26])
            users[row[0]]['quiz1']['histMoves'] = (row[27])
        else:
            print('warning - no has user name but has rows')


def readFromQuiz2A():
    csvFile = csv.reader(
        open(r"C:\Users\Shani Ben Haim\Desktop\quiz2.csv", "r"))
    for row in csvFile:
        if row[0] in users:
            #    users[row[0]] = userName
            users[row[0]]['quiz2']['minMoves'] = (row[1])
            users[row[0]]['quiz2']['firstBox'] = (row[2])
            users[row[0]]['quiz2']['secBox'] = (row[3])
            users[row[0]]['quiz2']['firstMoveRate'] = (row[4])
            users[row[0]]['quiz2']['secondMoveRate'] = (row[5])
            users[row[0]]['quiz2']['thirdMoveRate'] = (row[6])
            users[row[0]]['quiz2']['forthMoveRate'] = (row[7])
            users[row[0]]['quiz2']['fifthMoveRate'] = (row[8])
            users[row[0]]['quiz2']['firstBox1Rate'] = (row[9])
            users[row[0]]['quiz2']['firstBox2Rate'] = (row[10])
            users[row[0]]['quiz2']['firstBox3Rate'] = (row[11])
            users[row[0]]['quiz2']['firstBox4Rate'] = (row[12])
            users[row[0]]['quiz2']['firstBox5Rate'] = (row[13])
            users[row[0]]['quiz2']['firstBox6Rate'] = (row[14])
            users[row[0]]['quiz2']['secondBox1Rate'] = (row[15])
            users[row[0]]['quiz2']['secondBox2Rate'] = (row[16])
            users[row[0]]['quiz2']['secondBox3Rate'] = (row[17])
            users[row[0]]['quiz2']['secondBox4Rate'] = (row[18])
            users[row[0]]['quiz2']['secondBox5Rate'] = (row[19])
            users[row[0]]['quiz2']['secondBox6Rate'] = (row[20])
            users[row[0]]['quiz2']['resetNum'] = (row[21])
            users[row[0]]['quiz2']['firstBoxToMove'] = (row[22])
            users[row[0]]['quiz2']['endTime'] = (row[23])
            users[row[0]]['quiz2']['totalMoves'] = (row[24])
            users[row[0]]['quiz2']['histMoves'] = (row[25])
        else:
            print('warning - no has user name but has rows')


def readFromQuiz3A():
    csvFile = csv.reader(
        open(r"C:\Users\Shani Ben Haim\Desktop\quiz3.csv", "r"))
    for row in csvFile:
        if row[0] in users:
            #    users[row[0]] = userName
            users[row[0]]['quiz3']['minMoves'] = (row[1])
            users[row[0]]['quiz3']['firstBox'] = (row[2])
            users[row[0]]['quiz3']['secBox'] = (row[3])
            users[row[0]]['quiz3']['firstMoveRate'] = (row[4])
            users[row[0]]['quiz3']['secondMoveRate'] = (row[5])
            users[row[0]]['quiz3']['thirdMoveRate'] = (row[6])
            users[row[0]]['quiz3']['forthMoveRate'] = (row[7])
            users[row[0]]['quiz3']['fifthMoveRate'] = (row[8])
            users[row[0]]['quiz3']['firstBox1Rate'] = (row[9])
            users[row[0]]['quiz3']['firstBox2Rate'] = (row[10])
            users[row[0]]['quiz3']['firstBox3Rate'] = (row[11])
            users[row[0]]['quiz3']['firstBox4Rate'] = (row[12])
            users[row[0]]['quiz3']['firstBox5Rate'] = (row[13])
            users[row[0]]['quiz3']['firstBox6Rate'] = (row[14])
            users[row[0]]['quiz3']['secondBox1Rate'] = (row[15])
            users[row[0]]['quiz3']['secondBox2Rate'] = (row[16])
            users[row[0]]['quiz3']['secondBox3Rate'] = (row[17])
            users[row[0]]['quiz3']['secondBox4Rate'] = (row[18])
            users[row[0]]['quiz3']['secondBox5Rate'] = (row[19])
            users[row[0]]['quiz3']['secondBox6Rate'] = (row[20])
            users[row[0]]['quiz3']['resetNum'] = (row[21])
            users[row[0]]['quiz3']['firstBoxToMove'] = (row[22])
            users[row[0]]['quiz3']['endTime'] = (row[23])
            users[row[0]]['quiz3']['totalMoves'] = (row[24])
            users[row[0]]['quiz3']['histMoves'] = (row[25])
        else:
            print('warning - no has user name but has rows')


def deleteEmptyLines():
    for key, value in list(users.items()):
        flag = 'false'
        for key1, value1 in value.items():
            if flag == 'false':
                for key2, value2 in value1.items():
                    if value2 == '' and key2 != 'bonus':
                        flag = 'true'
                        del users[key]
                        break
            else:
                break


def calcDistTable(tableName, dictName):
    numOfRows = 0
    firstBox1Real = 0
    firstBox2Real = 0
    firstBox3Real = 0
    firstBox4Real = 0
    firstBox5Real = 0
    firstBox6Real = 0
    secBox1Real = 0
    secBox2Real = 0
    secBox3Real = 0
    secBox4Real = 0
    secBox5Real = 0
    secBox6Real = 0
    firstRangeReal = 0
    secRangeReal = 0
    thirdRangeReal = 0
    forthRangeReal = 0
    fifthRangeReal = 0
    firstBox1Rate = 0
    firstBox2Rate = 0
    firstBox3Rate = 0
    firstBox4Rate = 0
    firstBox5Rate = 0
    firstBox6Rate = 0
    secBox1Rate = 0
    secBox2Rate = 0
    secBox3Rate = 0
    secBox4Rate = 0
    secBox5Rate = 0
    secBox6Rate = 0
    firstRangeRate = 0
    secRangeRate = 0
    thirdRangeRate = 0
    forthRangeRate = 0
    fifthRangeRate = 0

    for key, value in dictName.items():
        numOfRows += 1
        for key1, value1 in value.items():
            if key1 == tableName:
                for key2, value2 in value1.items():
                    try:
                        value2 = float(value2)
                        if key2 == 'minMoves':
                            if value2 >= 0 and value2 <= 39:
                                firstRangeReal += 1
                            elif value2 >= 40 and value2 <= 79:
                                secRangeReal += 1
                            elif value2 >= 80 and value2 <= 109:
                                thirdRangeReal += 1
                            elif value2 >= 110 and value2 <= 139:
                                forthRangeReal += 1
                            elif value2 >= 140:
                                fifthRangeReal += 1
                            else:
                                print(value2)
                        elif key2 == 'firstBox':
                            if value2 == 1:
                                firstBox1Real += 1
                            elif value2 == 2:
                                firstBox2Real += 1
                            elif value2 == 3:
                                firstBox3Real += 1
                            elif value2 == 4:
                                firstBox4Real += 1
                            elif value2 == 5:
                                firstBox5Real += 1
                            elif value2 == 6:
                                firstBox6Real += 1
                            else:
                                print(value2)
                        elif key2 == 'secBox':
                            if value2 == 1:
                                secBox1Real += 1
                            elif value2 == 2:
                                secBox2Real += 1
                            elif value2 == 3:
                                secBox3Real += 1
                            elif value2 == 4:
                                secBox4Real += 1
                            elif value2 == 5:
                                secBox5Real += 1
                            elif value2 == 6:
                                secBox6Real += 1
                            else:
                                print(value2)
                        elif key2 == 'firstMoveRate':
                            firstRangeRate += value2
                        elif key2 == 'secondMoveRate':
                            secRangeRate += value2
                        elif key2 == 'thirdMoveRate':
                            thirdRangeRate += value2
                        elif key2 == 'forthMoveRate':
                            forthRangeRate += value2
                        elif key2 == 'fifthMoveRate':
                            fifthRangeRate += value2
                        elif key2 == 'firstBox1Rate':
                            firstBox1Rate += value2
                        elif key2 == 'firstBox2Rate':
                            firstBox2Rate += value2
                        elif key2 == 'firstBox3Rate':
                            firstBox3Rate += value2
                        elif key2 == 'firstBox4Rate':
                            firstBox4Rate += value2
                        elif key2 == 'firstBox5Rate':
                            firstBox5Rate += value2
                        elif key2 == 'firstBox6Rate':
                            firstBox6Rate += value2
                        elif key2 == 'secondBox1Rate':
                            secBox1Rate += value2
                        elif key2 == 'secondBox2Rate':
                            secBox2Rate += value2
                        elif key2 == 'secondBox3Rate':
                            secBox3Rate += value2
                        elif key2 == 'secondBox4Rate':
                            secBox4Rate += value2
                        elif key2 == 'secondBox5Rate':
                            secBox5Rate += value2
                        elif key2 == 'secondBox6Rate':
                            secBox6Rate += value2
                    except ValueError:
                        if value2 == 'minMoves':
                            numOfRows -= 1
                        print(value2)

    resultSet = {'numOfRows': numOfRows, 'firstBox1Real': firstBox1Real, 'firstBox2Real': firstBox2Real, 'firstBox3Real': firstBox3Real, 'firstBox4Real': firstBox4Real, 'firstBox5Real': firstBox5Real, 'firstBox6Real': firstBox6Real,
                 'secBox1Real': secBox1Real, 'secBox2Real': secBox2Real, 'secBox3Real': secBox3Real, 'secBox4Real': secBox4Real, 'secBox5Real': secBox5Real, 'secBox6Real': secBox6Real,
                 'firstRangeReal': firstRangeReal, 'secRangeReal': secRangeReal, 'thirdRangeReal': thirdRangeReal, 'forthRangeReal': forthRangeReal, 'fifthRangeReal': fifthRangeReal, 'firstBox1Rate': firstBox1Rate,
                 'firstBox2Rate': firstBox2Rate, 'firstBox3Rate': firstBox3Rate, 'firstBox4Rate': firstBox4Rate, 'firstBox5Rate': firstBox5Rate, 'firstBox6Rate': firstBox6Rate, 'secBox1Rate': secBox1Rate, 'secBox2Rate': secBox2Rate,
                 'secBox3Rate': secBox3Rate, 'secBox4Rate': secBox4Rate, 'secBox5Rate': secBox5Rate, 'secBox6Rate': secBox6Rate, 'firstRangeRate': firstRangeRate, 'secRangeRate': secRangeRate, 'thirdRangeRate': thirdRangeRate, 'forthRangeRate': forthRangeRate, 'fifthRangeRate': fifthRangeRate}

    return resultSet


def makeComparisonsForMinMovesCSV(resultSetGroup, groupName):
    with open('quiz3.csv', mode='a',newline='') as csv_file:
        fieldnames = ['group','firstMoveRate', 'secondMoveRate','thirdMoveRate', 'forthMoveRate', 'fifthMoveRate',
        'firstBox1Rate','firstBox2Rate','firstBox3Rate','firstBox4Rate','firstBox5Rate','firstBox6Rate',
        'secBox1Rate' ,'secBox2Rate' ,'secBox3Rate' ,'secBox4Rate' ,'secBox5Rate' ,'secBox6Rate',
        'firstRangeReal', 'secRangeReal', 'thirdRangeReal' , 'forthRangeReal', 'fifthRangeReal',
        'firstBox1Real','firstBox2Real','firstBox3Real','firstBox4Real','firstBox5Real','firstBox6Real',
        'secBox1Real','secBox2Real','secBox3Real','secBox4Real','secBox5Real','secBox6Real'
        ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        #writer.writeheader()

        if resultSetGroup['numOfRows'] != 0:
            writer.writerow({'group':groupName,
                            'firstMoveRate':  float(resultSetGroup['firstRangeRate']/resultSetGroup['numOfRows']),
                            'secondMoveRate': float(resultSetGroup['secRangeRate']/resultSetGroup['numOfRows']),
                            'thirdMoveRate': float(resultSetGroup['thirdRangeRate']/resultSetGroup['numOfRows']),
                            'forthMoveRate':  float(resultSetGroup['forthRangeRate']/resultSetGroup['numOfRows']),
                            'fifthMoveRate':  float(resultSetGroup['fifthRangeRate']/resultSetGroup['numOfRows']),

                            'firstBox1Rate': float(resultSetGroup['firstBox1Rate']/resultSetGroup['numOfRows']),
                            'firstBox2Rate': float(resultSetGroup['firstBox2Rate']/resultSetGroup['numOfRows']),
                            'firstBox3Rate':  float(resultSetGroup['firstBox3Rate']/resultSetGroup['numOfRows']),
                            'firstBox4Rate':  float(resultSetGroup['firstBox4Rate']/resultSetGroup['numOfRows']),
                            'firstBox5Rate':  float(resultSetGroup['firstBox5Rate']/resultSetGroup['numOfRows']),
                            'firstBox6Rate':  float(resultSetGroup['firstBox6Rate']/resultSetGroup['numOfRows']),

                            'secBox1Rate': float(resultSetGroup['secBox1Rate']/resultSetGroup['numOfRows']),
                            'secBox2Rate': float(resultSetGroup['secBox2Rate']/resultSetGroup['numOfRows']),
                            'secBox3Rate':  float(resultSetGroup['secBox3Rate']/resultSetGroup['numOfRows']),
                            'secBox4Rate':  float(resultSetGroup['secBox4Rate']/resultSetGroup['numOfRows']),
                            'secBox5Rate':  float(resultSetGroup['secBox5Rate']/resultSetGroup['numOfRows']),
                            'secBox6Rate':  float(resultSetGroup['secBox6Rate']/resultSetGroup['numOfRows']),

                            'firstRangeReal': float(resultSetGroup['firstRangeReal']/resultSetGroup['numOfRows'])*100,
                            'secRangeReal': float(resultSetGroup['secRangeReal']/resultSetGroup['numOfRows'])*100,
                            'thirdRangeReal': float(resultSetGroup['thirdRangeReal']/resultSetGroup['numOfRows'])*100,
                            'forthRangeReal': float(resultSetGroup['forthRangeReal']/resultSetGroup['numOfRows'])*100,
                            'fifthRangeReal': float(resultSetGroup['fifthRangeReal']/resultSetGroup['numOfRows'])*100,

                            'firstBox1Real': float(resultSetGroup['firstBox1Real']/resultSetGroup['numOfRows'])*100,
                            'firstBox2Real': float(resultSetGroup['firstBox2Real']/resultSetGroup['numOfRows'])*100,
                            'firstBox3Real': float(resultSetGroup['firstBox3Real']/resultSetGroup['numOfRows'])*100,
                            'firstBox4Real': float(resultSetGroup['firstBox4Real']/resultSetGroup['numOfRows'])*100,
                            'firstBox5Real': float(resultSetGroup['firstBox5Real']/resultSetGroup['numOfRows'])*100,
                            'firstBox6Real': float(resultSetGroup['firstBox6Real']/resultSetGroup['numOfRows'])*100,

                            'secBox1Real': float(resultSetGroup['secBox1Real']/resultSetGroup['numOfRows'])*100,
                            'secBox2Real': float(resultSetGroup['secBox2Real']/resultSetGroup['numOfRows'])*100,
                            'secBox3Real': float(resultSetGroup['secBox3Real']/resultSetGroup['numOfRows'])*100,
                            'secBox4Real': float(resultSetGroup['secBox4Real']/resultSetGroup['numOfRows'])*100,
                            'secBox5Real': float(resultSetGroup['secBox5Real']/resultSetGroup['numOfRows'])*100,
                            'secBox6Real': float(resultSetGroup['secBox6Real']/resultSetGroup['numOfRows'])*100,

                            })
        else:
            writer.writerow({'group':groupName,
                            'firstMoveRate':  0,
                            'secondMoveRate': 0,
                            'thirdMoveRate': 0,
                            'forthMoveRate': 0,
                            'fifthMoveRate': 0,
                            'firstBox1Rate':  0,
                            'firstBox2Rate': 0,
                            'firstBox3Rate': 0,
                            'firstBox4Rate': 0,
                            'firstBox5Rate': 0,
                            'firstBox6Rate': 0,

                            'secBox1Rate': 0,
                            'secBox2Rate': 0,
                            'secBox3Rate': 0,
                            'secBox4Rate': 0,
                            'secBox5Rate': 0,
                            'secBox6Rate': 0,

                            'firstRangeReal': 0,
                            'secRangeReal': 0,
                            'thirdRangeReal': 0,
                            'forthRangeReal': 0,
                            'fifthRangeReal': 0,

                            'firstBox1Real': 0,
                            'firstBox2Real': 0,
                            'firstBox3Real': 0,
                            'firstBox4Real':  0,
                            'firstBox5Real':  0,
                            'firstBox6Real':  0,

                            'secBox1Real': 0,
                            'secBox2Real':  0,
                            'secBox3Real': 0,
                            'secBox4Real':  0,
                            'secBox5Real':  0,
                            'secBox6Real': 0
                            })


def makeComparisonsForMinMoves(resultSetGroup, resultSetPop):
    if resultSetGroup['numOfRows'] != 0:
        groupPredictForMinMoves = {'firstMoveRate': float(resultSetGroup['firstRangeRate']/resultSetGroup['numOfRows']),
                                   'secondMoveRate': float(resultSetGroup['secRangeRate']/resultSetGroup['numOfRows']),
                                   'thirdMoveRate': float(resultSetGroup['thirdRangeRate']/resultSetGroup['numOfRows']),
                                   'forthMoveRate': float(resultSetGroup['forthRangeRate']/resultSetGroup['numOfRows']),
                                   'fifthMoveRate': float(resultSetGroup['fifthRangeRate']/resultSetGroup['numOfRows']),
                                   }
        realPredictForMinMoves = {'firstRangeReal': float(resultSetPop['firstRangeReal']/resultSetPop['numOfRows'])*100,
                                  'secRangeReal': float(resultSetPop['secRangeReal']/resultSetPop['numOfRows'])*100,
                                  'thirdRangeReal': float(resultSetPop['thirdRangeReal']/resultSetPop['numOfRows'])*100,
                                  'forthRangeReal': float(resultSetPop['forthRangeReal']/resultSetPop['numOfRows'])*100,
                                  'fifthRangeReal': float(resultSetPop['fifthRangeReal']/resultSetPop['numOfRows'])*100,
                                  }
        propDiff = {'firstRange': abs(float(groupPredictForMinMoves['firstMoveRate'] - realPredictForMinMoves['firstRangeReal'])),
                    'secRange': abs(float(groupPredictForMinMoves['secondMoveRate'] - realPredictForMinMoves['secRangeReal'])),
                    'thirdRange': abs(float(groupPredictForMinMoves['thirdMoveRate'] - realPredictForMinMoves['thirdRangeReal'])),
                    'forthRange': abs(float(groupPredictForMinMoves['forthMoveRate'] - realPredictForMinMoves['forthRangeReal'])),
                    'fifthRange': abs(float(groupPredictForMinMoves['fifthMoveRate'] - realPredictForMinMoves['fifthRangeReal'])),
                    }
        return propDiff
    return {}


def makeComparisonsForBox1(resultSetGroup, resultSetPop):
    if resultSetGroup['numOfRows'] != 0:
        groupPredictForMinMoves = {'box1Rate': float(resultSetGroup['firstBox1Rate']/resultSetGroup['numOfRows']),
                                   'box2Rate': float(resultSetGroup['firstBox2Rate']/resultSetGroup['numOfRows']),
                                   'box3Rate': float(resultSetGroup['firstBox3Rate']/resultSetGroup['numOfRows']),
                                   'box4Rate': float(resultSetGroup['firstBox4Rate']/resultSetGroup['numOfRows']),
                                   'box5Rate': float(resultSetGroup['firstBox5Rate']/resultSetGroup['numOfRows']),
                                   'box6Rate': float(resultSetGroup['firstBox6Rate']/resultSetGroup['numOfRows']),
                                   }
        realPredictForMinMoves = {'box1Real': float(resultSetPop['firstBox1Real']/resultSetPop['numOfRows'])*100,
                                  'box2Real': float(resultSetPop['firstBox2Real']/resultSetPop['numOfRows'])*100,
                                  'box3Real': float(resultSetPop['firstBox3Real']/resultSetPop['numOfRows'])*100,
                                  'box4Real': float(resultSetPop['firstBox4Real']/resultSetPop['numOfRows'])*100,
                                  'box5Real': float(resultSetPop['firstBox5Real']/resultSetPop['numOfRows'])*100,
                                  'box6Real': float(resultSetPop['firstBox6Real']/resultSetPop['numOfRows'])*100,
                                  }
        propDiff = {'box1': abs(float(groupPredictForMinMoves['box1Rate'] - realPredictForMinMoves['box1Real'])),
                    'box2': abs(float(groupPredictForMinMoves['box2Rate'] - realPredictForMinMoves['box2Real'])),
                    'box3': abs(float(groupPredictForMinMoves['box3Rate'] - realPredictForMinMoves['box3Real'])),
                    'box4': abs(float(groupPredictForMinMoves['box4Rate'] - realPredictForMinMoves['box4Real'])),
                    'box5': abs(float(groupPredictForMinMoves['box5Rate'] - realPredictForMinMoves['box5Real'])),
                    'box6': abs(float(groupPredictForMinMoves['box6Rate'] - realPredictForMinMoves['box6Real'])),
                    }
        return propDiff
    return {}


def makeComparisonsForBox2(resultSetGroup, resultSetPop):
    if resultSetGroup['numOfRows'] != 0:
        groupPredictForMinMoves = {'box1Rate': float(resultSetGroup['secBox1Rate']/resultSetGroup['numOfRows']),
                                   'box2Rate': float(resultSetGroup['secBox2Rate']/resultSetGroup['numOfRows']),
                                   'box3Rate': float(resultSetGroup['secBox3Rate']/resultSetGroup['numOfRows']),
                                   'box4Rate': float(resultSetGroup['secBox4Rate']/resultSetGroup['numOfRows']),
                                   'box5Rate': float(resultSetGroup['secBox5Rate']/resultSetGroup['numOfRows']),
                                   'box6Rate': float(resultSetGroup['secBox6Rate']/resultSetGroup['numOfRows']),
                                   }
        realPredictForMinMoves = {'box1Real': float(resultSetPop['secBox1Real']/resultSetPop['numOfRows'])*100,
                                  'box2Real': float(resultSetPop['secBox2Real']/resultSetPop['numOfRows'])*100,
                                  'box3Real': float(resultSetPop['secBox3Real']/resultSetPop['numOfRows'])*100,
                                  'box4Real': float(resultSetPop['secBox4Real']/resultSetPop['numOfRows'])*100,
                                  'box5Real': float(resultSetPop['secBox5Real']/resultSetPop['numOfRows'])*100,
                                  'box6Real': float(resultSetPop['secBox6Real']/resultSetPop['numOfRows'])*100,
                                  }
        propDiff = {'box1': abs(float(groupPredictForMinMoves['box1Rate'] - realPredictForMinMoves['box1Real'])),
                    'box2': abs(float(groupPredictForMinMoves['box2Rate'] - realPredictForMinMoves['box2Real'])),
                    'box3': abs(float(groupPredictForMinMoves['box3Rate'] - realPredictForMinMoves['box3Real'])),
                    'box4': abs(float(groupPredictForMinMoves['box4Rate'] - realPredictForMinMoves['box4Real'])),
                    'box5': abs(float(groupPredictForMinMoves['box5Rate'] - realPredictForMinMoves['box5Real'])),
                    'box6': abs(float(groupPredictForMinMoves['box6Rate'] - realPredictForMinMoves['box6Real'])),
                    }
        return propDiff
    return {}


def makeGroupsMinMoves(tableName):
    firstRangeGroup = {}
    secRangeGroup = {}
    thirdRangeGroup = {}
    forthRangeGroup = {}
    fifthRangeGroup = {}

    for key, value in users.items():
        for key1, value1 in value.items():
            if key1 == tableName:
                for key2, value2 in value1.items():
                    try:
                        value2 = float(value2)
                        if key2 == 'minMoves':
                            if value2 >= 0 and value2 <= 39:
                                firstRangeGroup[key] = value
                            elif value2 >= 40 and value2 <= 79:
                                secRangeGroup[key] = value
                            elif value2 >= 80 and value2 <= 109:
                                thirdRangeGroup[key] = value
                            elif value2 >= 110 and value2 <= 139:
                                forthRangeGroup[key] = value
                            elif value2 >= 140:
                                fifthRangeGroup[key] = value
                            else:
                                print(value2)
                    except ValueError:
                        print(value2)
    newGroup = {'firstRangeGroup': firstRangeGroup, 'secRangeGroup': secRangeGroup,
                'thirdRangeGroup': thirdRangeGroup, 'forthRangeGroup': forthRangeGroup,
                'fifthRangeGroup': fifthRangeGroup}
    return newGroup


def makeGroupsFirstBox(tableName):
    firstBox1Group = {}
    firstBox2Group = {}
    firstBox3Group = {}
    firstBox4Group = {}
    firstBox5Group = {}
    firstBox6Group = {}

    for key, value in users.items():
        for key1, value1 in value.items():
            if key1 == tableName:
                for key2, value2 in value1.items():
                    try:
                        value2 = float(value2)
                        if key2 == 'firstBox':
                            if value2 == 1:
                                firstBox1Group[key] = value
                            elif value2 == 2:
                                firstBox2Group[key] = value
                            elif value2 == 3:
                                firstBox3Group[key] = value
                            elif value2 == 4:
                                firstBox4Group[key] = value
                            elif value2 == 5:
                                firstBox5Group[key] = value
                            elif value2 == 6:
                                firstBox6Group[key] = value
                            else:
                                print(value2)
                    except ValueError:
                        print(value2)
    newGroup = {'firstBox1Group': firstBox1Group, 'firstBox2Group': firstBox2Group,
                'firstBox3Group': firstBox3Group, 'firstBox4Group': firstBox4Group,
                'firstBox5Group': firstBox5Group, 'firstBox6Group': firstBox6Group}
    return newGroup


def makeGroupsSecBox(tableName):
    secBox1Group = {}
    secBox2Group = {}
    secBox3Group = {}
    secBox4Group = {}
    secBox5Group = {}
    secBox6Group = {}

    for key, value in users.items():
        for key1, value1 in value.items():
            if key1 == tableName:
                for key2, value2 in value1.items():
                    try:
                        value2 = float(value2)
                        if key2 == 'secBox':
                            if value2 == 1:
                                secBox1Group[key] = value
                            elif value2 == 2:
                                secBox2Group[key] = value
                            elif value2 == 3:
                                secBox3Group[key] = value
                            elif value2 == 4:
                                secBox4Group[key] = value
                            elif value2 == 5:
                                secBox5Group[key] = value
                            elif value2 == 6:
                                secBox6Group[key] = value
                            else:
                                print(value2)
                    except ValueError:
                        print(value2)
    newGroup = {'secBox1Group': secBox1Group, 'secBox2Group': secBox2Group,
                'secBox3Group': secBox3Group, 'secBox4Group': secBox4Group,
                'secBox5Group': secBox5Group, 'secBox6Group': secBox6Group}
    return newGroup


def whoClosetFor(resultSets, answerTocheck):
    distanceArr = []
    for row in resultSets:
        if row != {}:
            distanceArr.append(row[answerTocheck])
    return min(distanceArr)


def whoClosetAllBoxes(resultSets):
    distanceArr = []
    for propDiff in resultSets:
        if propDiff != {}:
            distanceArr.append(math.sqrt((propDiff['box1']**2) + (propDiff['box2']**2) + (
                propDiff['box3']**2) + (propDiff['box4']**2) + (propDiff['box5']**2) + (propDiff['box6']**2)))
    return min(distanceArr)


def whoClosetAllMinMoves(resultSets):
    distanceArr = []
    for propDiff in resultSets:
        if propDiff != {}:
            distanceArr.append(math.sqrt((propDiff['firstRange']**2) + (propDiff['secRange']**2) + (
                propDiff['thirdRange']**2) + (propDiff['forthRange']**2) + (propDiff['fifthRange']**2)))
    return min(distanceArr)


def makeGroupWithout(groupToDel):
    newGroup = {}
    for row in users:
        if row not in groupToDel:
            newGroup[row] = users[row]
    return newGroup


def innerCrowd():
    icUsers = {}
    for key, value in users.items():
        for key1, value1 in value.items():
            if key != 'UserName':
                icUsers[key]= {'quiz1MM':users[key]['quiz1']['minMoves'] , 'quiz1FB' :users[key]['quiz1']['firstBox'],'quiz1SB' :users[key]['quiz1']['secBox'],
                'quiz2MM':users[key]['quiz2']['minMoves'] , 'quiz2FB' :users[key]['quiz2']['firstBox'],'quiz2SB' :users[key]['quiz2']['secBox'],
                'quiz3MM':users[key]['quiz3']['minMoves'] , 'quiz3FB' :users[key]['quiz3']['firstBox'],'quiz3SB' :users[key]['quiz3']['secBox']
                }
    with open('ic.csv', mode='a',newline='') as csv_file:
        fieldnames = ['userName','quiz1MM','quiz1FB', 'quiz1SB','quiz2MM', 'quiz2FB', 'quiz2SB', 'quiz3MM','quiz3FB','quiz3SB' ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in icUsers:
            writer.writerow({'userName':row, 'quiz1MM':icUsers[row]['quiz1MM'],'quiz1FB':icUsers[row]['quiz1FB'],'quiz1SB':icUsers[row]['quiz1SB'],
            'quiz2MM':icUsers[row]['quiz2MM'],'quiz2FB':icUsers[row]['quiz2FB'],'quiz2SB':icUsers[row]['quiz2SB'],
            'quiz3MM':icUsers[row]['quiz3MM'],'quiz3FB':icUsers[row]['quiz3FB'],'quiz3SB':icUsers[row]['quiz3SB']})



def checkQuiz2():
    quiz2RS = calcDistTable('quiz2', users)
    newMinMovesQuiz2Group = makeGroupsMinMoves('quiz2')
    newFirstBoxQuiz2Group = makeGroupsFirstBox('quiz2')
    newSecBoxQuiz2Group = makeGroupsSecBox('quiz2')

    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newMinMovesQuiz2Group['firstRangeGroup'])),'firstRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newMinMovesQuiz2Group['secRangeGroup'])), 'secRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newMinMovesQuiz2Group['thirdRangeGroup'])), 'thirdRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newMinMovesQuiz2Group['forthRangeGroup'])), 'forthRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newMinMovesQuiz2Group['fifthRangeGroup'])), 'fifthRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newFirstBoxQuiz2Group['firstBox1Group'])),'firstBox1GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newFirstBoxQuiz2Group['firstBox2Group'])), 'firstBox2GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newFirstBoxQuiz2Group['firstBox3Group'])), 'firstBox3GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newFirstBoxQuiz2Group['firstBox4Group'])), 'firstBox4GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newFirstBoxQuiz2Group['firstBox5Group'])), 'firstBox5GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newFirstBoxQuiz2Group['firstBox6Group'])), 'firstBox6GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newSecBoxQuiz2Group['secBox1Group'])),'secBox1GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newSecBoxQuiz2Group['secBox2Group'])), 'secBox2GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newSecBoxQuiz2Group['secBox3Group'])), 'secBox3GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newSecBoxQuiz2Group['secBox4Group'])), 'secBox4GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newSecBoxQuiz2Group['secBox5Group'])), 'secBox5GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', makeGroupWithout(newSecBoxQuiz2Group['secBox6Group'])), 'secBox6GroupWithout')
    ##
    makeComparisonsForMinMovesCSV(quiz2RS, 'All')
    ##with!
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newMinMovesQuiz2Group['firstRangeGroup']),'firstRange')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newMinMovesQuiz2Group['secRangeGroup']), 'secRange')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newMinMovesQuiz2Group['thirdRangeGroup']), 'thirdRange')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newMinMovesQuiz2Group['forthRangeGroup']), 'forthRange')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newMinMovesQuiz2Group['fifthRangeGroup']), 'fifthRange')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newFirstBoxQuiz2Group['firstBox1Group']), 'firstBox1')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newFirstBoxQuiz2Group['firstBox2Group']), 'firstBox2')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newFirstBoxQuiz2Group['firstBox3Group']), 'firstBox3')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newFirstBoxQuiz2Group['firstBox4Group']), 'firstBox4')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newFirstBoxQuiz2Group['firstBox5Group']), 'firstBox5')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newFirstBoxQuiz2Group['firstBox6Group']), 'firstBox6')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newSecBoxQuiz2Group['secBox1Group']), 'secBox1')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newSecBoxQuiz2Group['secBox2Group']), 'secBox2')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newSecBoxQuiz2Group['secBox3Group']), 'secBox3')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newSecBoxQuiz2Group['secBox4Group']), 'secBox4')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newSecBoxQuiz2Group['secBox5Group']), 'secBox5')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz2', newSecBoxQuiz2Group['secBox6Group']), 'secBox6')

def checkQuiz3():
    quiz2RS = calcDistTable('quiz3', users)
    newMinMovesQuiz3Group = makeGroupsMinMoves('quiz3')
    newFirstBoxQuiz3Group = makeGroupsFirstBox('quiz3')
    newSecBoxQuiz3Group = makeGroupsSecBox('quiz3')

    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newMinMovesQuiz3Group['firstRangeGroup'])),'firstRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newMinMovesQuiz3Group['secRangeGroup'])), 'secRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newMinMovesQuiz3Group['thirdRangeGroup'])), 'thirdRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newMinMovesQuiz3Group['forthRangeGroup'])), 'forthRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newMinMovesQuiz3Group['fifthRangeGroup'])), 'fifthRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newFirstBoxQuiz3Group['firstBox1Group'])),'firstBox1GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newFirstBoxQuiz3Group['firstBox2Group'])), 'firstBox2GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newFirstBoxQuiz3Group['firstBox3Group'])), 'firstBox3GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newFirstBoxQuiz3Group['firstBox4Group'])), 'firstBox4GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newFirstBoxQuiz3Group['firstBox5Group'])), 'firstBox5GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newFirstBoxQuiz3Group['firstBox6Group'])), 'firstBox6GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newSecBoxQuiz3Group['secBox1Group'])),'secBox1GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newSecBoxQuiz3Group['secBox2Group'])), 'secBox2GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newSecBoxQuiz3Group['secBox3Group'])), 'secBox3GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newSecBoxQuiz3Group['secBox4Group'])), 'secBox4GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newSecBoxQuiz3Group['secBox5Group'])), 'secBox5GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', makeGroupWithout(newSecBoxQuiz3Group['secBox6Group'])), 'secBox6GroupWithout')
    ##
    makeComparisonsForMinMovesCSV(quiz2RS, 'All')
    ##with!
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newMinMovesQuiz3Group['firstRangeGroup']),'firstRange')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newMinMovesQuiz3Group['secRangeGroup']), 'secRange')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newMinMovesQuiz3Group['thirdRangeGroup']), 'thirdRange')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newMinMovesQuiz3Group['forthRangeGroup']), 'forthRange')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newMinMovesQuiz3Group['fifthRangeGroup']), 'fifthRange')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newFirstBoxQuiz3Group['firstBox1Group']), 'firstBox1')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newFirstBoxQuiz3Group['firstBox2Group']), 'firstBox2')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newFirstBoxQuiz3Group['firstBox3Group']), 'firstBox3')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newFirstBoxQuiz3Group['firstBox4Group']), 'firstBox4')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newFirstBoxQuiz3Group['firstBox5Group']), 'firstBox5')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newFirstBoxQuiz3Group['firstBox6Group']), 'firstBox6')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newSecBoxQuiz3Group['secBox1Group']), 'secBox1')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newSecBoxQuiz3Group['secBox2Group']), 'secBox2')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newSecBoxQuiz3Group['secBox3Group']), 'secBox3')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newSecBoxQuiz3Group['secBox4Group']), 'secBox4')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newSecBoxQuiz3Group['secBox5Group']), 'secBox5')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz3', newSecBoxQuiz3Group['secBox6Group']), 'secBox6')


def checkQuiz1():
    # createDistTable
    quiz1RS = calcDistTable('quiz1', users)

    # groups for first box and compare for real in quiz1
    """
    newFirstBoxQuiz1Group = makeGroupsFirstBox('quiz1')
    quiz1FirstB1 = makeComparisonsForBox1(calcDistTable('quiz1', newFirstBoxQuiz1Group['firstBox1Group']), quiz1RS)
    quiz1FirstB2 = makeComparisonsForBox1(calcDistTable('quiz1', newFirstBoxQuiz1Group['firstBox2Group']), quiz1RS)
    quiz1FirstB3 = makeComparisonsForBox1(calcDistTable('quiz1', newFirstBoxQuiz1Group['firstBox3Group']), quiz1RS)
    quiz1FirstB4 = makeComparisonsForBox1(calcDistTable('quiz1', newFirstBoxQuiz1Group['firstBox4Group']), quiz1RS)
    quiz1FirstB5 = makeComparisonsForBox1(calcDistTable('quiz1', newFirstBoxQuiz1Group['firstBox5Group']), quiz1RS)
    quiz1FirstB6 = makeComparisonsForBox1(calcDistTable('quiz1', newFirstBoxQuiz1Group['firstBox6Group']), quiz1RS)    
    compareAllBoxes = makeComparisonsForBox1(quiz1RS, quiz1RS)
    """
    newFirstBoxQuiz1Group = makeGroupsMinMoves('quiz1')
    newFirstBoxQuiz1Group3 = makeGroupsFirstBox('quiz1')
    newFirstBoxQuiz1Group2 = makeGroupsSecBox('quiz1')
    """
    quiz1FirstB1 = makeComparisonsForMinMoves(calcDistTable(
        'quiz1', newFirstBoxQuiz1Group['firstRangeGroup']), quiz1RS)
    quiz1FirstB2 = makeComparisonsForMinMoves(calcDistTable(
        'quiz1', newFirstBoxQuiz1Group['secRangeGroup']), quiz1RS)
    quiz1FirstB3 = makeComparisonsForMinMoves(calcDistTable(
        'quiz1', newFirstBoxQuiz1Group['thirdRangeGroup']), quiz1RS)
    quiz1FirstB4 = makeComparisonsForMinMoves(calcDistTable(
        'quiz1', newFirstBoxQuiz1Group['forthRangeGroup']), quiz1RS)
    quiz1FirstB5 = makeComparisonsForMinMoves(calcDistTable(
        'quiz1', newFirstBoxQuiz1Group['fifthRangeGroup']), quiz1RS)
    compareAllMoves = makeComparisonsForMinMoves(quiz1RS, quiz1RS)
    """
    #without!
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group['firstRangeGroup'])),'firstRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable(  'quiz1', makeGroupWithout(newFirstBoxQuiz1Group['secRangeGroup'])), 'secRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable(  'quiz1', makeGroupWithout(newFirstBoxQuiz1Group['thirdRangeGroup'])), 'thirdRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable(  'quiz1', makeGroupWithout(newFirstBoxQuiz1Group['forthRangeGroup'])), 'forthRangeWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group['fifthRangeGroup'])), 'fifthRangeWithout')
    
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group3['firstBox1Group'])),'firstBox1GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group3['firstBox2Group'])), 'firstBox2GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group3['firstBox3Group'])), 'firstBox3GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group3['firstBox4Group'])), 'firstBox4GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group3['firstBox5Group'])), 'firstBox5GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group3['firstBox6Group'])), 'firstBox6GroupWithout')
    
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group2['secBox1Group'])),'secBox1GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group2['secBox2Group'])), 'secBox2GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group2['secBox3Group'])), 'secBox3GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group2['secBox4Group'])), 'secBox4GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group2['secBox5Group'])), 'secBox5GroupWithout')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', makeGroupWithout(newFirstBoxQuiz1Group2['secBox6Group'])), 'secBox6GroupWithout')
    
    ##
    makeComparisonsForMinMovesCSV(quiz1RS, 'All')
    ##with!
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group['firstRangeGroup']),'firstRange')
    makeComparisonsForMinMovesCSV(calcDistTable(
        'quiz1', newFirstBoxQuiz1Group['secRangeGroup']), 'secRange')
    makeComparisonsForMinMovesCSV(calcDistTable(
        'quiz1', newFirstBoxQuiz1Group['thirdRangeGroup']), 'thirdRange')
    makeComparisonsForMinMovesCSV(calcDistTable(
        'quiz1', newFirstBoxQuiz1Group['forthRangeGroup']), 'forthRange')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group['fifthRangeGroup']), 'fifthRange')
    
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group3['firstBox1Group']), 'firstBox1')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group3['firstBox2Group']), 'firstBox2')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group3['firstBox3Group']), 'firstBox3')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group3['firstBox4Group']), 'firstBox4')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group3['firstBox5Group']), 'firstBox5')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group3['firstBox6Group']), 'firstBox6')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group2['secBox1Group']), 'secBox1')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group2['secBox2Group']), 'secBox2')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group2['secBox3Group']), 'secBox3')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group2['secBox4Group']), 'secBox4')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group2['secBox5Group']), 'secBox5')
    makeComparisonsForMinMovesCSV(calcDistTable('quiz1', newFirstBoxQuiz1Group2['secBox6Group']), 'secBox6')

    # compare all groups to all answers
    #minForAllAnswers = whoClosetAllBoxes([compareAllBoxes])
    #minForAllAnswers1 = whoClosetAllMinMoves([compareAllMoves])

    """
    #compare all groups to specific answer
    minForAllAnswers2 = whoClosetFor([compareAllBoxes], 'box3')
    minForAllAnswers3 = whoClosetFor([compareAllMoves], 'firstRange')
    """

    """
    # compare group to all answers
    minForAllAnswers4 = whoClosetAllMinMoves(
        [quiz1FirstB1, quiz1FirstB2, quiz1FirstB3, quiz1FirstB4, quiz1FirstB5])

    # compare group to specific answer
    minForAllAnswers5 = whoClosetFor(
        [quiz1FirstB1, quiz1FirstB2, quiz1FirstB3, quiz1FirstB4, quiz1FirstB5], 'firstRange')
    minForAllAnswers6 = whoClosetFor(
        [quiz1FirstB1, quiz1FirstB2, quiz1FirstB3, quiz1FirstB4, quiz1FirstB5], 'secRange')
    minForAllAnswers7 = whoClosetFor(
        [quiz1FirstB1, quiz1FirstB2, quiz1FirstB3, quiz1FirstB4, quiz1FirstB5], 'thirdRange')
    minForAllAnswers8 = whoClosetFor(
        [quiz1FirstB1, quiz1FirstB2, quiz1FirstB3, quiz1FirstB4, quiz1FirstB5], 'forthRange')
    minForAllAnswers9 = whoClosetFor(
        [quiz1FirstB1, quiz1FirstB2, quiz1FirstB3, quiz1FirstB4, quiz1FirstB5], 'fifthRange')
    """
    DS = 'ER'


def readCSV():
    readFromUsersA()
    readFromQuiz1A()
    readFromQuiz2A()
    readFromQuiz3A()
    readFromBQ12A()
    readFromBQ23A()
    deleteEmptyLines()
    #innerCrowd()
    #checkQuiz1()
    #checkQuiz2()
    checkQuiz3()

    return users
