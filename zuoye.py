# -*- coding:utf-8 -*-
import random
import sys

class Usage(Exception):
    def __init__(self,msg):
        self.msg =msg

def func_add():
    a = random.randint(1,30)
    b = random.randint(1,50-a)
    #print repr(a).rjust(4),' + ',repr(b).rjust(3),' = '
    fo = open("shuxuezuoye.txt","a")
    fo.write(repr(a).rjust(4) + '+'.rjust(3) + repr(b).rjust(4) + '='.rjust(2))
    fo.close()
    return

def func_sub():
    a = random.randint(10,50)
    b = random.randint(1,a)
    #print repr(a).rjust(4),'-'.rjust(4),repr(b).rjust(3),'='.rjust(4)
    fo = open("shuxuezuoye.txt","a")
    fo.write(repr(a).rjust(4) + '-'.rjust(3) + repr(b).rjust(4) + '='.rjust(2))
    fo.close()
    return

def main():
    print "准备生成数学作业"
    number = int(input("题目数量是："))
    fo = open("shuxuezuoye.txt","wb")
    fo.write("数学作业,共 "+ repr(number) +" 题\n")
    fo.close()
    while number > 0:
        if random.randint(0,1):
            func_add()
        else:
            func_sub();
        fo = open("shuxuezuoye.txt","a")
        if number%2 == 1:
            fo.write('\n' + '||'.rjust(22) + '\n' + '||'.rjust(22) + '\n' + '||'.rjust(22) + '\n' + '||'.rjust(22) + '\n')
        else:
            fo.write('       ||       ')
        fo.close()
        number = number - 1  
    return
#print a ,"+", b

if __name__ == '__main__':
    main()
