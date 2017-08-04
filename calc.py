def error(str='Error expression.'):
    print str
    exit(1)
def lex(str):
    ret,i=[],0
    while i < len(str):
    	word=''
        if str[i] in '+-*/^()':
            word=str[i]
            i+=1
        elif str[i].isdigit():
            hasdot=False
            while i < len(str):
                if str[i]=='.':
                	if not hasdot:
                		hasdot=True;
                	else:
                		error('Two dots?')
                elif not str[i].isdigit():
                	break
                word+=str[i]
                i+=1
        else:
            error("Unexpect '%s'."%str[i])
        ret.append(word)
    return ret
at=0
def exp_5(lis):
    global at
    if lis[at][0].isdigit():
        at+=1
        return float(lis[at-1])
    if lis[at]=='(':
        at+=1
        ret=exp_1(lis)
        if lis[at]==')':
            at+=1
            return ret
        else:
            error()
    else:
        error()
def exp_4(lis):
    global at
    if lis[at]=='+':
        at+=1
        return exp_5(lis)
    elif lis[at]=='-':
        at+=1
        return -exp_5(lis)
    else:
        return exp_5(lis)

def exp_3(lis):
    global at
    a=exp_4(lis)
    if at >= len(lis):
        return a
    while lis[at]=='^':
        at+=1
        a=pow(a,exp_3(lis))
        if at >= len(lis):
            break
    return a
def exp_2(lis):
    global at
    a=exp_3(lis)
    if at >= len(lis):
        return a
    while lis[at] in '*/' :
        if lis[at]=='*':
            at+=1
            a*=exp_3(lis)
        elif lis[at]=='/':
            at+=1
            a/=exp_3(lis)
        if at >= len(lis):
            break
    return a
def exp_1(lis):
    global at
    a=exp_2(lis)
    if at >= len(lis):
        return a
    while lis[at] in '+-':
        if lis[at]=='+':
            at+=1
            a+=exp_2(lis)
        elif lis[at]=='-':
            at+=1
            a-=exp_2(lis)
        if at >= len(lis):
            break
    return a
def parse(lis):
    return exp_1(lis)
while True:
    at,i=0,1
    str=raw_input('%d >'%i)
    result=parse(lex(str))
    print '..',result
    i+=1