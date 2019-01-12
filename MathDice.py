# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:59:05 2015

@author: WAM
"""

ops={0:'+',1:'-',2:'*',3:'/',4:'^',5:'^1/'}

def operation(num1,num2,op):
    #carry out the operation specified
    #0=+ 1=- 2=* 3=/ 4=** 5=root
    num1=float(num1)
    num2=float(num2)
    try:
        if op==0:
            result=num1+num2
        elif op==1:
            result=num1-num2
        elif op==2:
            result=num1*num2
        elif op==3:
            # if num2==0:
            #     result=float('nan')
            # else:
            result=num1/num2
        elif op==4:
            result=num1**num2
        else:
            # if (num2==0 or num1<0):
            #     result=float('nan')
            # else:
            result=num1**(1./num2)
    except:
        result = float('nan')
    return result

import itertools,math

roll=[0,0,0]
while True:
    roll[0]=int(input('d1: '))
    roll[1]=int(input('d2: '))
    roll[2]=int(input('d3: '))
    target=int(input('target d1: '))
    target*=int(input('target d2: '))
    #roll=(5,5,2)
    #1target=70
    
    closest=float('nan')
    #iterate over permutations of the dice
    for it in itertools.permutations(roll,3):
        #iterate over operations
        for op1 in range(0,6):
            for op2 in range(0,6):
                tempResult=operation(it[0],it[1],op1)
                result=operation(tempResult,it[2],op2)
                if not(abs(target-closest)<=abs(target-result) or math.isnan(result)):
                    closest=result
                    resultIt=it
                    resultOp1=op1
                    resultOp2=op2
                    l2r=True
                tempResult=operation(it[1],it[2],op2)
                result=operation(it[0],tempResult,op1)
                if not(abs(target-closest)<=abs(target-result) or math.isnan(result)):
                    closest=result
                    resultIt=it
                    resultOp1=op1
                    resultOp2=op2
                    l2r=False
    print('{0:g}'.format(closest))
    outStr=''
    if l2r:
        outStr+='('
    outStr+=str(resultIt[0])+ops[resultOp1]
    if not(l2r):
        outStr+='('
    outStr+=str(resultIt[1])
    if l2r:
        outStr+=')'
    outStr+=ops[resultOp2]+str(resultIt[2])
    if not(l2r):
        outStr+=')'
    print(outStr)
