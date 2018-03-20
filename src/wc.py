import sys
import re
import os
import tkFileDialog


reload(sys)
sys.setdefaultencoding("utf-8")

def judge(par, file, out='result.txt'):
    if par == '-c':
        with open(file, 'r') as f:
            count = 0
            while f.read(1):
                count += 1
            with open(out, 'a') as fm:
                fm.write(file + ',字符数：' + str(count) + '\n')
    if par == '-w':
        with open(file, 'r') as f:
            count = 0
            for line in f:
                sp = re.split(',|\x20', line)
                for i in sp:
                    if i not in table:
                        count += 1
            with open(out, 'a') as fn:
                fn.write(file + ',单词数：' + str(count) + '\n')
    if par == '-l':
        with open(file, 'r') as f:
            count = 0
            for line in f:
                count += 1
            with open(out, 'a') as fl:
                fl.write(file + ',行数：' + str(count) + '\n')
    if par == '-a':
        with open(file,'r') as f:
            c1,c2,c3=0,0,0
            for line in f:
                pattern2 = re.compile(r'.?\n')
                if pattern2.match(line):
                    c2+=1
                else:
                    line=line.strip()
                    pattern3 = re.compile(r'^(})?//')
                    pattern4 = re.compile(r'^(})?/\*')
                    pattern5 = re.compile(r'^\*/$')
                    if pattern3.match(line) or pattern4.match(line) or pattern5.match(line):
                        c3 += 1
                    else:
                        c1 += 1
            with open(out,'a') as fo:
                fo.write(file + ',代码行/空行/注释行：' + str(c1) +'/' + str(c2)+ '/'+str(c3) + '\n')

# judge(sys.argv[1],sys.argv[2])
para = []
i = 1
LEN = len(sys.argv)

table = []
if i <=(LEN-1) and sys.argv[i] == '-x':
    default_dir = r"CC:\Python27\PyInstaller-3.3.1\wc\dist"  # 设置默认打开目录
    fname = tkFileDialog.askopenfilename(title=u"选择文件", initialdir=(os.path.expanduser(default_dir)))
    for i2 in ['-c','-w','-l','-a']:
        judge(i2,fname,'outputFile.txt')
    os._exit(0)
while sys.argv[i] in ['-c', '-w', '-l', '-s','-a']:
    para.append(sys.argv[i])
    i += 1

ip = i
i += 1


if i <= (LEN - 1) and sys.argv[i] == '-e':
    i += 1
    if i <= (LEN - 1):
        with open(sys.argv[i], 'r') as f:
            i += 1
            for line in f:
                for SP in re.split(',|\x20', line):
                    table.append(SP)
    else:
        print("输入错误")

if i <= (LEN - 1) and sys.argv[i] == '-o':
    # print sys.argv[i]
    i += 1
    if i <= (LEN - 1):
        if '-s' not in para:
            for j in para:
                judge(j, sys.argv[ip], sys.argv[i])
        else:
            para.remove('-s')
            # files = os.listdir(sys.argv[ip])
            FILES = []
            for root, dirs, files in os.walk(sys.argv[ip], topdown=True):
                for name in files:
                    FILES.append(os.path.join(root, name))
            res = []
            for file in FILES:
                pattern = re.compile(r'.*\.c')
                if pattern.match(file):
                    res.append(file)
            for j in para:
                for k in res:
                    judge(j, k, sys.argv[i])

    else:
        print("输入错误")
else:
    if '-s' not in para:
        for j in para:
            judge(j, sys.argv[ip])
    else:
        para.remove('-s')
        # files = os.listdir(sys.argv[ip])
        FILES = []
        for root, dirs, files in os.walk(sys.argv[ip], topdown=True):
            for name in files:
                FILES.append(os.path.join(root, name))
        res = []
        for file in FILES:
            pattern = re.compile(r'.*\.c')
            if pattern.match(file):
                res.append(file)
        for j in para:
            for k in res:
                judge(j, k)
