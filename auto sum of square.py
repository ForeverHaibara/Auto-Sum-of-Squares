'''
Author: ForeverHaibara
'''

import sympy as sp


def rationalize(num):
    '''
    将 num 视为sympy的分数(Rational) 并返回
    '''
    try:
        if '.' in num:
            a = int(num.split('.')[0])
            exponent = 10**len(num.split('.')[1])
            b = int(num.split('.')[1])
            return sp.Rational(a*exponent+b if a>=0 else a*exponent-b,exponent)
        elif '/' in num:
            a = int(num.split('/')[0])
            b = int(num.split('/')[1])
            return sp.Rational(a,b)
        else :
            a = int(num)
            return sp.Rational(a,1)

    except:
        return sp.Rational(0,1)



def manufacture(f):
    '''
    补充函数字符串中省略的乘号 ，并将小数写成分数
    '''
    flag = True
    while flag:
        for i in range(1,len(f)):
            if ( f[i] == 'x' or f[i] == '(') and 48 <= ord(f[i-1]) <= 57:
                f = f[:i] + '*' + f[i:]
                break
        else :
            flag = False

    flag = True
    while flag:
        for i in range(len(f)):
            if f[i] == '.':
                for j1 in range(i-1,-1,-1):
                    if ord(f[j1]) < 48 or ord(f[j1]) > 57:
                        j1 += 1
                        break
                for j2 in range(i+1,len(f)):
                    if ord(f[j2]) < 48 or ord(f[j2]) > 57:
                        break
                else:
                    j2 += 1
                    
                exponent = 10**(j2-i-1)
                frac1 = int(f[j1:i])
                if frac1 >= 0:
                    f = f[:j1] + str(frac1*exponent+int(f[i+1:j2])) + '/' +str(exponent) + f[j2:]
                else:
                    f = f[:j1] + str(frac1*exponent-int(f[i+1:j2])) + '/' +str(exponent) + f[j2:]
                break
        else:
            flag = False
    
    return sp.fraction(sp.cancel(sp.sympify(f)))


def dominant(f):
    '''
    返回 sympy函数多项式 的最高次项和系数
    '''
    t = list(sp.Poly(f).as_dict().keys())[-1]
    return t[0] , sp.Poly(f).as_dict()[t]


def SOS(function,pos,left='0'):
    '''
    配方
    '''
    pos = rationalize(pos)
    left = rationalize(left)
    
    x = sp.Symbol('x')
    origin_function = sp.expand(sp.sympify(function))
    
    for try_times in range(1):
        function = origin_function
        deg , coeff = dominant(function)
        memo = [] 
        if coeff < 0:
            break

        while deg > 2:
            balance = 0
            leftv = function.subs(x,left)
            
            if coeff < 0:
                break

            if deg&1 == 1 : # odd
                try_function = coeff * (x-left) * (x-pos)**(deg-1)
                while try_function.subs(x,left) > leftv and balance < deg:
                    balance += 2
                    try_function = coeff * ((x-left)**(balance+1)) * (x-pos)**(deg-1-balance)
                
            else :
                try_function = coeff * (x-pos)**(deg)
                while try_function.subs(x,left) > leftv and balance <= deg:
                    balance += 2
                    try_function = coeff * ((x-left)**balance) * (x-pos)**(deg-balance)
            
            memo.append(try_function)
            function = function - sp.collect(sp.expand(try_function),x)

            try:
                deg , coeff = dominant(function)
            except:
                break
        
        if coeff < 0:
            break

        try:
            remains = sp.Poly(function).as_dict()
        except:
            remains = {}

        a = [0]*3
        for i in range(3):
            if (i,) in remains.keys():
                a[i] = remains[(i,)]

        #print('%lf(x-%lf)^2 + %lfx'%(a**0.5, (c/a)**0.5, b+((a*c)**0.5)*2))
        if (a[2]>=0 and a[1]*a[1] <= 4*a[2]*a[0]):
            for func in memo:
                print(func,end=' + ')
                
            print(' (',function,')')
            print('其中，二次函数部分 △ = b*b-4*a*c = ',a[1]*a[1]-4*a[2]*a[0],'<= 0 ')
            print('因此函数 >=0 , 证毕')
            return True
    

    for func in memo:
        print(func,end=' + ')
    print(' (',function,')')
    print("尝试失败")
                


x = sp.Symbol('x')

while True:
    myfunc = input("请输入一个自变量为x的有理函数:\n")
    try :
        myfunc, frac2 = manufacture(myfunc)
        print('通分化简后= (',myfunc,')/( ',frac2,')')
        left = input("请输入您要考察的左边界（默认为0）: ")
        x = input("请输入猜根近似值（默认为0）: ")
        print('上式分子= ')
        SOS(myfunc,x,left=left)

    except:
        print("输入错误，程序结束")
        break
    print('\n\n')
