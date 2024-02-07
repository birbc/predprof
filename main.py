class studentik:
    fio=''
    score=0
f=open('students.csv')
students=[]
f.readline()
for i in f:
    s=i.split(',')
    if s[3][:-1]=='10':
        a = studentik()
        fi=s[1].split()
        a.fio = fi[1][0]+'. '+fi[0]
        a.score = int(s[4])
        students.append(a)
for i in range(len(students)):
    j = i
    t = students[i]
    while j>0 and students[j-1].score<t.score:
        students[j]=students[j-1]
        j-=1
    students[j]=t
print('10 класс:')
print('1 место:', students[0].fio)
print('2 место:', students[1].fio)
print('3 место:', students[2].fio)
