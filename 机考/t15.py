"""
假设渊子原来一个BBS上的密码为zvbo9441987,为了方便记忆，他通过一种算法把这个密码变换成YUANzhi1987，这个密码是他的名字和出生年份，
怎么忘都忘不了，而且可以明目张胆地放在显眼的地方而不被别人知道真正的密码。
他是这么变换的，大家都知道手机上的字母： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,
就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换，
声明：密码中没有空格，而密码中出现的大写字母则变成小写之后往后移一位，如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。记住，z往后移是a哦。


"""
out = []
list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

while True:
    try:
        sr = input()
        for i in sr:
            if i in list1:
                out.append(i)
            elif i.isupper() and i != 'Z':
                out.append(chr(ord(i.lower())+1))
            elif i == 'Z':
                out.append('a')
            elif i in 'abc':
                out.append('2')
            elif i in 'def':
                out.append('3')
            elif i in 'ghi':
                out.append('4')
            elif i in 'jkl':
                out.append('5')
            elif i in 'mno':
                out.append('6')
            elif i in 'pqrs':
                out.append('7')
            elif i in 'tuv':
                out.append('8')
            elif i in 'wxyz':
                out.append('9')
        print(''.join(out))

    except:
        break
