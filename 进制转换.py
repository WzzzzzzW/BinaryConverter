while True:
    a = int(input("输入待转值:"))
    d = int(input("代转值是几进制:"))
    b = int(input("转换成几进制:"))
    s = [] #一个空列表，用来存储模
    c=""   #输出值
    e = 0  #a转化为10进制的数
    f = 1  #计算权值  
    for i in str(a):
        e +=int(i)*d**(len(str(a))-f)
        f+=1
    if b<=36:
        while e>=b:
            s.append(e%b)
            e //= b 
        s.append(e)
        for i in range(len(s)):
            if s[i] >=10:
                s[i] = chr(s[i]+55)
        for i in s:
            c = str(i)+c  
        print("输出值：",c)
    else:
        print("最大只支持转化到36进制!!")

