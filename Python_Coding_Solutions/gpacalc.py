import sys

sys.argv[0]
sys.argv[1]
sys.argv[2]
sys.argv[3]
sys.argv[4]

def gpacalc():
    sub1=str(sys.argv[1]).upper()
    sub2=str(sys.argv[2]).upper()
    sub3=str(sys.argv[3]).upper()
    sub4=str(sys.argv[4]).upper()

    grading = {'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, 'C':2.0, 'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}
    
    total = float(grading[sub1]) + float(grading[sub2]) + float(grading[sub3]) + float(grading[sub4])

    gpa = total / 4
 
    print ('%.2f'%gpa)

gpacalc()