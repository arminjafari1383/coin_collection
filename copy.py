# a,b = [int(a) for a in input("Please enter two values for variables ").split()]
# total = a * b
# print(f"copy of" + "  " + total)



# number max
# x = int(input(""))+
# a = int(input(""))
# for i in range(a):
#     y = []
#     y.append(input("enter the number"))
# print(max(y))


#inverse number
# def reverse_number(n):
#     r = 0
#     while n > 0:
#         r *= 10
#         r += n % 10
#         n /= 10
#     return r

# print(reverse_number(121))
# دریافت ورودی
num1 = input().strip()
num2 = input().strip()

# برعکس کردن اعداد
rev_num1 = num1[::-1]
rev_num2 = num2[::-1]

# مقایسه اعداد برعکس شده و چاپ نتیجه
if rev_num1 < rev_num2:
    print(f"{num1} < {num2}")
elif rev_num1 > rev_num2:
    print(f"{num2} < {num1}")
else:
    print(f"{num1} = {num2}")
