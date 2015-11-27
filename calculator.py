# -*- coding: utf-8 -*-

print "选择运算："
print "1.相加"
print "2.相减"
print "3.相乘"
print "4.相除"

choice = input("输入你的选择(1/2/3/4)：")

num1 = int(input("输入第一个数字："))
num2 = int(input("输入第二个数字："))

if choice == '1':
    print "%d + %d = ％d)" % (num1, num2, num1 + num2)
    
elif choice == '2':
    print "%d - %d = %d" % (num1, num2, num1 - num2)

elif choice == '3':
    print "%d * %d = %d" % (num1, num2, num1 * num2)

elif choice == '4':
    print "%d / %d = %d" % (num1, num2, num1 / num2)

else:
    print "非法输入"