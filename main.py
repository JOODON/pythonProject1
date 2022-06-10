from Score import *

# 작업 선택 종류
SEARCH, LIST, STATS, DATAMG, END = ('1', '2', '3', '4', 'x')


def sel_task():  # 작업 선택 메뉴
    print("_" * 50)
    print("1:검색   2:현황   3:통계   4:데이터관리   x:종료")
    selno = input("<작업 선택> ")
    if len(selno) == 0:
        return 'x'
    else:
        return selno


def find_student():
    instid = input(">학번 입력: ")
    val = get_student(instid)
    sname, deptid = val  # 리스트 언팩킹
    dname = get_dept(deptid)
    print("학번: %s    성명: %s   소속학과: %s(%s)" % (instid, sname, dname, deptid))


def selmenu01_find():
    while True:
        print("_" * 50)
        print("1: 학생검색    2: 학과검색    3: 교수검색    4: 과목검색    5: 성적검색    0: 복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                find_student()
            elif selno == 2:
                find_dept()
            elif selno == 3:
                find_prof()
            elif selno == 4:
                find_subject()
            elif selno == 5:
                find_stscore()
            elif selno == 0:
                sel_task()
            else:
                print("!잘못된 입력!")


def List01_find():
    while True:
        print("_" * 50)
        print("1:학생 성적 현황(학생 성적 통지서) 2.과목별 성적 현황 0.복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                all_List()
            elif selno == 2:
                List_subject1()
            elif selno == 0:
                sel_task()
            else:
                print("!잘못된 입력!")


def STATS01_find():
    while True:
        print("_" * 50)
        print("1:과목별 성적 통계 2.교수별 담당 과목 0.복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                stats_find()
            elif selno == 2:
                stats_find2()
            elif selno == 0:
                sel_task()
            else:
                print("!잘못된 입력!")


###########################################################2###################################################################
def find_student():
    instid = input(">학번 입력: ")
    val = get_student(instid)
    sname, deptid = val  # 리스트 언팩킹
    dname = get_dept(deptid)
    print("학번: %s    성명: %s   소속학과: %s(%s)" % (instid, sname, dname, deptid))


def find_dept():
    indeptid = input(">학과 번호 입력:")
    dname = get_dept(indeptid)
    print("학과명 :%s (%s)" % (dname, indeptid))


def find_prof():
    prof = input(">검색할 교수님을 입력:")
    dname = get_prof(prof)
    name, age = dname
    print("교수님 성함 :%s (%s)" % (name, age))


def find_subject():
    insubject = input(">검색할 과목을 입력:")
    subject = get_subject(insubject)
    study, time, fulltime, FirstName = subject
    print("[과목명:%s] [학점 : %s] [개설 학과:%s] [ProF:%s]" % (study, time, fulltime, FirstName))


def find_stscore():
    instscore = input(">[학번]을 입력 해주세요")
    for number, studynumber, score in stscore:
        if instscore == number:
            print("[번호 :%s] [과목 번호:%s] [점수:%s]" % (number, studynumber, score))


###########################################################2###################################################################
def all_List():
    instid = input(">학번 입력: ")
    val = get_student(instid)
    sname, deptid = val
    dname = get_dept(deptid)
    print("[학번: %s]    [성명: %s]   [소속학과: %s(%s)]" % (instid, sname, dname, deptid))
    count = 0
    counttime = 0
    Average = 0
    sumscore = 0
    for number, studynumber, score in stscore:
        subject = get_subject(studynumber)
        study, time, fulltime, FirstName = subject
        ascore = int(score)
        if ascore <= 100 and ascore >= 95:
            rank = "A+"
        elif ascore < 95 and ascore >= 90:
            rank = "A"
        elif ascore < 90 and ascore >= 85:
            rank = "B+"
        elif ascore < 85 and ascore >= 80:
            rank = "B"
        elif ascore < 80 and ascore >= 75:
            rank = "C+"
        elif ascore < 75 and ascore >= 70:
            rank = "C"
        elif ascore < 70 and ascore >= 65:
            rank = "D+"
        elif ascore < 65 and ascore >= 60:
            rank = "D"
        else:
            rank = "F"
        if number == instid:
            print("[과목명:%s] [과목코드 : %s] [학점:%s] [점수:%s] [등급:%s]" % (study, studynumber, time, score, rank))
            count += 1
            times = int(time)  ##학점을 더해주기 위해 형 변환
            counttime = counttime + times  ##총 학점 수
            sumscore = sumscore + int(score)  ##평균을 구하기 위해 형 변환
            Average = sumscore / count  ##평균 값

            credit = 0
            sumcredit = 0
            if Average >= 95:
                credit = 4.5
                rank = "A+"
            elif Average >= 90:
                credit = 4.0
                rank = "A"
            elif Average >= 85:
                credit = 3.5
                rank = "B+"
            elif Average >= 80:
                credit = 3.0
                rank = "B"
            elif Average >= 75:
                credit = 2.5
                rank = "C+"
            elif Average >= 70:
                credit = 2.0
                rank = "C"
            elif Average >= 65:
                credit = 1.5
                rank = "D"
            elif Average >= 60:
                credit = 1.0
                rank = "D+"
            else:
                credit = 0
    print("[과목 수:%d] [학점 수:%d] [평균 점수: %d] [평점%.1f]" % (count, counttime, Average, float(credit)))


def List_subject1():
    insubject = input(">검색할 과목코드를 입력해주세요:")
    subject = get_subject(insubject)
    study, time, fulltime, FirstName = subject
    dname = get_prof(FirstName)  ##교수님 이름
    name, age = dname
    dname = get_dept(fulltime)  ##학과 딕셔너리
    print("[과목명:%s] [과목코드: %s][학점 : %s] [개설 학과:%s] [교수님 이름:%s]" % (study, insubject, time, dname, name))
    studycount = 0
    fullscore = 0
    for number, studynumber, score in stscore:
        if studynumber == insubject:
            studycount += 1
            val = get_student(number)
            sname, deptid = val  # 리스트 언팩킹
            dname = get_dept(deptid)
            ascore = float(score)
            fullscore = fullscore + ascore
            if ascore <= 100 and ascore >= 95:
                rank = "A+"
            elif ascore < 95 and ascore >= 90:
                rank = "A"
            elif ascore < 90 and ascore >= 85:
                rank = "B+"
            elif ascore < 85 and ascore >= 80:
                rank = "B"
            elif ascore < 80 and ascore >= 75:
                rank = "C+"
            elif ascore < 75 and ascore >= 70:
                rank = "C"
            elif ascore < 70 and ascore >= 65:
                rank = "D+"
            elif ascore < 65 and ascore >= 60:
                rank = "D"
            else:
                rank = "F"
            print("[학생성명:%s][학번:%s][점수:%s][등급:%s]" % (sname, number, score, rank))
            Average = fullscore / studycount  ##평균 값
            if Average >= 95:
                credit = 4.5
                rank = "A+"
            elif Average >= 90:
                credit = 4.0
                rank = "A"
            elif Average >= 85:
                credit = 3.5
                rank = "B+"
            elif Average >= 80:
                credit = 3.0
                rank = "B"
            elif Average >= 75:
                credit = 2.5
                rank = "C+"
            elif Average >= 70:
                credit = 2.0
                rank = "C"
            elif Average >= 65:
                credit = 1.5
                rank = "D"
            elif Average >= 60:
                credit = 1.0
                rank = "D+"
            else:
                credit = 0
    print("[학생 수:%s] [평균 점수:%.1f] [평점%.1f]" % (studycount, float(fullscore / studycount), credit))


###########################################3##########################################################################

def stats_find():
        indeptid = input(">학과 번호 입력:")
        dname = get_dept(indeptid)
        print("[학과명 :%s (%s)]" % (dname, indeptid))
        for scode,val in subject.items():
            studyname,time,studycode,Nikname=val
            if indeptid in studycode:
                arr = []
                count = 0
                Avarge = 0
                allArv = 0
                for number, studynumber, score in stscore:
                    if scode in studynumber:
                        ascore=int(score)
                        arr.append(ascore)
                        Avarge=Avarge+ascore
                        count+=1
                print("[과목명:%s] [과목코드:%s] [학점:%s] [수강생 수:%d] [평균 점수:%d] [최고점수:%d] [최저점수:%d]" %(studyname,studynumber,time,count,Avarge/count,max(arr),min(arr)))


def stats_find2():
    indeptid = input(">학과 번호 입력:")
    dname = get_dept(indeptid)
    print("학과명 :%s (%s)" % (dname, indeptid))
    count=0
    for nikname,val in prof.items():##교수님 분류
        name,age=val##나이랑 이름 분류
        for dcode,val1 in subject.items():##학생이랑 이름 나이를 분류
            studyname,time,studycode,nik=val1##과목 이름 학점 학과번호 닉네임으로 분류
    print("[교수아이디:%s] [교수명:%s] [과목명:%s] [학점:%s] [수강생 수:%d]" % (nikname, name, studyname, time, count))





########## Main ################
while True:  # 작업 선택
    selno = sel_task()  # 작업 번호 선택
    if selno == SEARCH:
        selmenu01_find()
    elif selno == LIST:
        List01_find()
    elif selno == STATS:
        STATS01_find()
    elif selno == DATAMG:
        selmenu04_up()
    elif selno == END:  # (x)끝내기
        break
    else:
        break
################################
