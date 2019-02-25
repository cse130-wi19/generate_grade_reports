from fpdf import FPDF
import sys,os

def generate_template():
    pdf = FPDF()
    pdf.set_font('Times', '', 15)
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.ln(0)
    pdf.cell(0, 10, 'Name: ', 0, 1)
    pdf.cell(0, 10, 'PID: ', 0, 1)
    pdf.cell(0, 10, 'ieng6 username: ', 0, 1)
    pdf.cell(0, 10, 'Grade: ', 0, 1)
    # for i in range(1, 41):
    #     pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
    pdf.output('template.pdf', 'F')    

def parse_student_list(fileN):
    f=open(fileN).read().split('\n')
    stList={}
    for i in f:
        elems=i.split(',')
        stList[elems[0]]=elems[1:]  # elems[0] is ieng6 acc id
                                    # rest it is in order: PID,Last Name,First Name,UCSD Email Address
    return stList

def parse_marks(fileN):
    f=open(fileN).read().split('\n')
    stMarks={}
    for i in f:
        tmp=i.split(",")
        if(len(tmp)<2):
            continue
        if tmp[0]=="USER" and tmp[1]=="SCORE":
            continue
        
        stMarks[tmp[0]]=tmp[1]
    return stMarks

def generate_grade_pdf(stList,stMarks):
    pdf = FPDF()
    pdf.set_font('Times', '', 15)
    pdf.alias_nb_pages()
    for i in stMarks:
        if(i not in stList):
            print("userid::"+i+"not found in student list")
            exit()
        pdf.add_page()
        pdf.ln(0)
        ieng6_uname=i
        uName=stList[i][2]+" "+stList[i][1]
        pid=stList[i][0]
        grade=stMarks[i]
        pdf.cell(0, 10, 'Name:   '+uName, 0, 1)
        pdf.cell(0, 10, 'PID:   '+pid, 0, 1)
        pdf.cell(0, 10, 'ieng6 username:   '+ ieng6_uname, 0, 1)
        pdf.cell(0, 10, 'Grade:   '+grade, 0, 1)
    pdf.output('grade.pdf', 'F')

if __name__== "__main__":
    generate_template()
    if (len(sys.argv)<3):
        print("Usage:: python grade.py <csv for ieng mapping> <allresult.csv>")
        exit()
    stList=parse_student_list(sys.argv[1])
    stMarks=parse_marks(sys.argv[2])
    generate_grade_pdf(stList,stMarks)
    # print(stList)