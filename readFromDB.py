import mysql.connector
import pandas
from pandas import DataFrame

mydb = mysql.connector.connect(
    host="quizagdm.coxqxrjsrdck.us-east-1.rds.amazonaws.com",
    database='gdma',
    user="admin",
    passwd="admingdma")


def writeUsersA():
    sql_select_Query = "select * from UsersA"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    userNameRecords = []
    workerIDRecords = []
    ageRecords = []
    genderRecords = []
    educationRecords = []
    bonusRecords = []
    for row in records:
        userNameRecords.append(row[0])
        workerIDRecords.append(row[1])
        ageRecords.append(row[2])
        genderRecords.append(row[3])
        educationRecords.append(row[4])
        bonusRecords.append(row[5])

    C = {'UserName': userNameRecords,
         'WorkerID': workerIDRecords,
         'age': ageRecords,
         'gender': genderRecords,
         'education': educationRecords,
         'bonus': bonusRecords
         }
    df = pandas.DataFrame(C, columns=['UserName', 'WorkerID',
                                      'age', 'gender', 'education', 'bonus'])
    export_csv = df.to_csv(
        r'C:\Users\Shani Ben Haim\Desktop\demog.csv', mode='a', index=None, header=True)

    cursor.close()


def writeBQ12A():
    sql_select_Query = "select * from BQ12A"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    userNameRecords = []
    minMovesRecords = []
    firstBoxRecords = []
    secondBoxRecords = []
    resetNumRecords = []
    firstBoxToMoveRecords = []
    endTimeRecords = []
    totalMovesRecords = []
    histMovesRecords = []

    for row in records:
        userNameRecords.append(row[0])
        minMovesRecords.append(row[1])
        firstBoxRecords.append(row[2])
        secondBoxRecords.append(row[3])
        resetNumRecords.append(row[4])
        firstBoxToMoveRecords.append(row[5])
        endTimeRecords.append(row[6])
        totalMovesRecords.append(row[7])
        histMovesRecords.append(row[8])

    D = {'UserName': userNameRecords,
         'minMoves': minMovesRecords,
         'firstBox': firstBoxRecords,
         'secBox': secondBoxRecords,
         'resetNum': resetNumRecords,
         'firstBoxToMove': firstBoxToMoveRecords,
         'endTime': endTimeRecords,
         'totalMoves': totalMovesRecords,
         'histMoves': histMovesRecords
         }
    df = pandas.DataFrame(D, columns=['UserName', 'minMoves',
                                      'firstBox', 'secBox', 'resetNum', 'firstBoxToMove', 'endTime', 'totalMoves', 'histMoves'])
    export_csv = df.to_csv(
        r'C:\Users\Shani Ben Haim\Desktop\bq12.csv', mode='a', index=None, header=True)

    cursor.close()


def writeBQ23A():
    sql_select_Query = "select * from BQ23A"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    userNameRecords = []
    minMovesRecords = []
    firstBoxRecords = []
    secondBoxRecords = []
    resetNumRecords = []
    firstBoxToMoveRecords = []
    endTimeRecords = []
    totalMovesRecords = []
    histMovesRecords = []

    for row in records:
        userNameRecords.append(row[0])
        minMovesRecords.append(row[1])
        firstBoxRecords.append(row[2])
        secondBoxRecords.append(row[3])
        resetNumRecords.append(row[4])
        firstBoxToMoveRecords.append(row[5])
        endTimeRecords.append(row[6])
        totalMovesRecords.append(row[7])
        histMovesRecords.append(row[8])

    D = {'UserName': userNameRecords,
         'minMoves': minMovesRecords,
         'firstBox': firstBoxRecords,
         'secBox': secondBoxRecords,
         'resetNum': resetNumRecords,
         'firstBoxToMove': firstBoxToMoveRecords,
         'endTime': endTimeRecords,
         'totalMoves': totalMovesRecords,
         'histMoves': histMovesRecords
         }
    df = pandas.DataFrame(D, columns=['UserName', 'minMoves',
                                      'firstBox', 'secBox', 'resetNum', 'firstBoxToMove', 'endTime', 'totalMoves', 'histMoves'])
    export_csv = df.to_csv(
        r'C:\Users\Shani Ben Haim\Desktop\bq23.csv', mode='a', index=None, header=True)

    cursor.close()


def writeQuiz1A():
    sql_select_Query = "select * from Quiz1A"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    userNameRecords = []
    minMovesRecords = []
    firstBoxRecords = []
    secondBoxRecords = []
    hardmeRecords = []
    hardthemRecords = []
    firstMoveRateRecords = []
    secMoveRateRecords = []
    thirdMoveRateRecords = []
    forthMoveRateRecords = []
    fifthMoveRateRecords = []
    firstBox1RateRecords = []
    firstBox2RateRecords = []
    firstBox3RateRecords = []
    firstBox4RateRecords = []
    firstBox5RateRecords = []
    firstBox6RateRecords = []
    secondBox1RateRecords = []
    secondBox2RateRecords = []
    secondBox3RateRecords = []
    secondBox4RateRecords = []
    secondBox5RateRecords = []
    secondBox6RateRecords = []
    resetNumRecords = []
    firstBoxToMoveRecords = []
    endTimeRecords = []
    totalMovesRecords = []
    histMovesRecords = []

    for row in records:
        userNameRecords.append(row[0])
        minMovesRecords.append(row[1])
        firstBoxRecords.append(row[2])
        secondBoxRecords.append(row[3])
        hardmeRecords.append(row[4])
        hardthemRecords.append(row[5])
        firstMoveRateRecords.append(row[6])
        secMoveRateRecords.append(row[7])
        thirdMoveRateRecords.append(row[8])
        forthMoveRateRecords.append(row[9])
        fifthMoveRateRecords.append(row[10])
        firstBox1RateRecords.append(row[11])
        firstBox2RateRecords.append(row[12])
        firstBox3RateRecords.append(row[13])
        firstBox4RateRecords.append(row[14])
        firstBox5RateRecords.append(row[15])
        firstBox6RateRecords.append(row[16])
        secondBox1RateRecords.append(row[17])
        secondBox2RateRecords.append(row[18])
        secondBox3RateRecords.append(row[19])
        secondBox4RateRecords.append(row[20])
        secondBox5RateRecords.append(row[21])
        secondBox6RateRecords.append(row[22])
        resetNumRecords.append(row[23])
        firstBoxToMoveRecords.append(row[24])
        endTimeRecords.append(row[25])
        totalMovesRecords.append(row[26])
        histMovesRecords.append(row[27])

    D = {'UserName': userNameRecords,
         'minMoves': minMovesRecords,
         'firstBox': firstBoxRecords,
         'secBox': secondBoxRecords,
         'hardme': hardmeRecords,
         'hardthem': hardthemRecords,
         'firstMoveRate': firstMoveRateRecords,
         'secondMoveRate': secMoveRateRecords,
         'thirdMoveRate': thirdMoveRateRecords,
         'forthMoveRate': forthMoveRateRecords,
         'fifthMoveRate': fifthMoveRateRecords,
         'firstBox1Rate': firstBox1RateRecords,
         'firstBox2Rate': firstBox2RateRecords,
         'firstBox3Rate': firstBox3RateRecords,
         'firstBox4Rate': firstBox4RateRecords,
         'firstBox5Rate': firstBox5RateRecords,
         'firstBox6Rate': firstBox6RateRecords,
         'secondBox1Rate': secondBox1RateRecords,
         'secondBox2Rate': secondBox2RateRecords,
         'secondBox3Rate': secondBox3RateRecords,
         'secondBox4Rate': secondBox4RateRecords,
         'secondBox5Rate': secondBox5RateRecords,
         'secondBox6Rate': secondBox6RateRecords,
         'resetNum': resetNumRecords,
         'firstBoxToMove': firstBoxToMoveRecords,
         'endTime': endTimeRecords,
         'totalMoves': totalMovesRecords,
         'histMoves': histMovesRecords
         }
    df = pandas.DataFrame(D, columns=['UserName', 'minMoves', 'firstBox', 'secBox',
                                      'hardme', 'hardthem', 'firstMoveRate', 'secondMoveRate', 'thirdMoveRate', 'forthMoveRate', 'fifthMoveRate',  'firstBox1Rate', 'firstBox2Rate', 'firstBox3Rate', 'firstBox4Rate',
                                      'firstBox5Rate',  'firstBox6Rate', 'secondBox1Rate',  'secondBox2Rate', 'secondBox3Rate', 'secondBox4Rate',
                                      'secondBox5Rate',  'secondBox6Rate', 'resetNum', 'firstBoxToMove', 'endTime', 'totalMoves', 'histMoves'])
    export_csv = df.to_csv(
        r'C:\Users\Shani Ben Haim\Desktop\quiz1.csv', mode='a', index=None, header=True)

    cursor.close()


def writeQuiz2A():
    sql_select_Query = "select * from Quiz2A"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    userNameRecords = []
    minMovesRecords = []
    firstBoxRecords = []
    secondBoxRecords = []
    firstMoveRateRecords = []
    secMoveRateRecords = []
    thirdMoveRateRecords = []
    forthMoveRateRecords = []
    fifthMoveRateRecords = []
    firstBox1RateRecords = []
    firstBox2RateRecords = []
    firstBox3RateRecords = []
    firstBox4RateRecords = []
    firstBox5RateRecords = []
    firstBox6RateRecords = []
    secondBox1RateRecords = []
    secondBox2RateRecords = []
    secondBox3RateRecords = []
    secondBox4RateRecords = []
    secondBox5RateRecords = []
    secondBox6RateRecords = []
    resetNumRecords = []
    firstBoxToMoveRecords = []
    endTimeRecords = []
    totalMovesRecords = []
    histMovesRecords = []

    for row in records:
        userNameRecords.append(row[0])
        minMovesRecords.append(row[1])
        firstBoxRecords.append(row[2])
        secondBoxRecords.append(row[3])
        firstMoveRateRecords.append(row[4])
        secMoveRateRecords.append(row[5])
        thirdMoveRateRecords.append(row[6])
        forthMoveRateRecords.append(row[7])
        fifthMoveRateRecords.append(row[8])
        firstBox1RateRecords.append(row[9])
        firstBox2RateRecords.append(row[10])
        firstBox3RateRecords.append(row[11])
        firstBox4RateRecords.append(row[12])
        firstBox5RateRecords.append(row[13])
        firstBox6RateRecords.append(row[14])
        secondBox1RateRecords.append(row[15])
        secondBox2RateRecords.append(row[16])
        secondBox3RateRecords.append(row[17])
        secondBox4RateRecords.append(row[18])
        secondBox5RateRecords.append(row[19])
        secondBox6RateRecords.append(row[20])
        resetNumRecords.append(row[21])
        firstBoxToMoveRecords.append(row[22])
        endTimeRecords.append(row[23])
        totalMovesRecords.append(row[24])
        histMovesRecords.append(row[25])

    D = {'UserName': userNameRecords,
         'minMoves': minMovesRecords,
         'firstBox': firstBoxRecords,
         'secBox': secondBoxRecords,
         'firstMoveRate': firstMoveRateRecords,
         'secondMoveRate': secMoveRateRecords,
         'thirdMoveRate': thirdMoveRateRecords,
         'forthMoveRate': forthMoveRateRecords,
         'fifthMoveRate': fifthMoveRateRecords,
         'firstBox1Rate': firstBox1RateRecords,
         'firstBox2Rate': firstBox2RateRecords,
         'firstBox3Rate': firstBox3RateRecords,
         'firstBox4Rate': firstBox4RateRecords,
         'firstBox5Rate': firstBox5RateRecords,
         'firstBox6Rate': firstBox6RateRecords,
         'secondBox1Rate': secondBox1RateRecords,
         'secondBox2Rate': secondBox2RateRecords,
         'secondBox3Rate': secondBox3RateRecords,
         'secondBox4Rate': secondBox4RateRecords,
         'secondBox5Rate': secondBox5RateRecords,
         'secondBox6Rate': secondBox6RateRecords,
         'resetNum': resetNumRecords,
         'firstBoxToMove': firstBoxToMoveRecords,
         'endTime': endTimeRecords,
         'totalMoves': totalMovesRecords,
         'histMoves': histMovesRecords
         }
    df = pandas.DataFrame(D, columns=['UserName', 'minMoves', 'firstBox', 'secBox',
                                      'firstMoveRate', 'secondMoveRate', 'thirdMoveRate', 'forthMoveRate', 'fifthMoveRate',  'firstBox1Rate', 'firstBox2Rate', 'firstBox3Rate', 'firstBox4Rate',
                                      'firstBox5Rate',  'firstBox6Rate', 'secondBox1Rate',  'secondBox2Rate', 'secondBox3Rate', 'secondBox4Rate',
                                      'secondBox5Rate',  'secondBox6Rate', 'resetNum', 'firstBoxToMove', 'endTime', 'totalMoves', 'histMoves'])
    export_csv = df.to_csv(
        r'C:\Users\Shani Ben Haim\Desktop\quiz2.csv', mode='a', index=None, header=True)

    cursor.close()

def writeQuiz3A():
    sql_select_Query = "select * from Quiz3A"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    userNameRecords = []
    minMovesRecords = []
    firstBoxRecords = []
    secondBoxRecords = []
    firstMoveRateRecords = []
    secMoveRateRecords = []
    thirdMoveRateRecords = []
    forthMoveRateRecords = []
    fifthMoveRateRecords = []
    firstBox1RateRecords = []
    firstBox2RateRecords = []
    firstBox3RateRecords = []
    firstBox4RateRecords = []
    firstBox5RateRecords = []
    firstBox6RateRecords = []
    secondBox1RateRecords = []
    secondBox2RateRecords = []
    secondBox3RateRecords = []
    secondBox4RateRecords = []
    secondBox5RateRecords = []
    secondBox6RateRecords = []
    resetNumRecords = []
    firstBoxToMoveRecords = []
    endTimeRecords = []
    totalMovesRecords = []
    histMovesRecords = []

    for row in records:
        userNameRecords.append(row[0])
        minMovesRecords.append(row[1])
        firstBoxRecords.append(row[2])
        secondBoxRecords.append(row[3])
        firstMoveRateRecords.append(row[4])
        secMoveRateRecords.append(row[5])
        thirdMoveRateRecords.append(row[6])
        forthMoveRateRecords.append(row[7])
        fifthMoveRateRecords.append(row[8])
        firstBox1RateRecords.append(row[9])
        firstBox2RateRecords.append(row[10])
        firstBox3RateRecords.append(row[11])
        firstBox4RateRecords.append(row[12])
        firstBox5RateRecords.append(row[13])
        firstBox6RateRecords.append(row[14])
        secondBox1RateRecords.append(row[15])
        secondBox2RateRecords.append(row[16])
        secondBox3RateRecords.append(row[17])
        secondBox4RateRecords.append(row[18])
        secondBox5RateRecords.append(row[19])
        secondBox6RateRecords.append(row[20])
        resetNumRecords.append(row[21])
        firstBoxToMoveRecords.append(row[22])
        endTimeRecords.append(row[23])
        totalMovesRecords.append(row[24])
        histMovesRecords.append(row[25])

    D = {'UserName': userNameRecords,
         'minMoves': minMovesRecords,
         'firstBox': firstBoxRecords,
         'secBox': secondBoxRecords,
         'firstMoveRate': firstMoveRateRecords,
         'secondMoveRate': secMoveRateRecords,
         'thirdMoveRate': thirdMoveRateRecords,
         'forthMoveRate': forthMoveRateRecords,
         'fifthMoveRate': fifthMoveRateRecords,
         'firstBox1Rate': firstBox1RateRecords,
         'firstBox2Rate': firstBox2RateRecords,
         'firstBox3Rate': firstBox3RateRecords,
         'firstBox4Rate': firstBox4RateRecords,
         'firstBox5Rate': firstBox5RateRecords,
         'firstBox6Rate': firstBox6RateRecords,
         'secondBox1Rate': secondBox1RateRecords,
         'secondBox2Rate': secondBox2RateRecords,
         'secondBox3Rate': secondBox3RateRecords,
         'secondBox4Rate': secondBox4RateRecords,
         'secondBox5Rate': secondBox5RateRecords,
         'secondBox6Rate': secondBox6RateRecords,
         'resetNum': resetNumRecords,
         'firstBoxToMove': firstBoxToMoveRecords,
         'endTime': endTimeRecords,
         'totalMoves': totalMovesRecords,
         'histMoves': histMovesRecords
         }
    df = pandas.DataFrame(D, columns=['UserName', 'minMoves', 'firstBox', 'secBox',
                                      'firstMoveRate', 'secondMoveRate', 'thirdMoveRate', 'forthMoveRate', 'fifthMoveRate',  'firstBox1Rate', 'firstBox2Rate', 'firstBox3Rate', 'firstBox4Rate',
                                      'firstBox5Rate',  'firstBox6Rate', 'secondBox1Rate',  'secondBox2Rate', 'secondBox3Rate', 'secondBox4Rate',
                                      'secondBox5Rate',  'secondBox6Rate', 'resetNum', 'firstBoxToMove', 'endTime', 'totalMoves', 'histMoves'])
    export_csv = df.to_csv(
        r'C:\Users\Shani Ben Haim\Desktop\quiz3.csv', mode='a', index=None, header=True)

    cursor.close()
