# # دریافت ورودی
# num1 = input().strip()
# num2 = input().strip()

# # برعکس کردن اعداد
# rev_num1 = num1[::-1]
# rev_num2 = num2[::-1]

# # مقایسه اعداد برعکس شده و چاپ نتیجه
# if rev_num1 < rev_num2:
#     print(f"{num1} < {num2}")
# elif rev_num1 > rev_num2:
#     print(f"{num2} < {num1}")
# else:
#     print(f"{num1} = {num2}")
# num1 = input().strip()
# num2 = input().strip()
# rev_num1 = num1[::-1]
# rev_num2 = num2[::-1]
# if rev_num1 < rev_num2:
#     print(f"{num1} < {num2}")
# elif rev_num1 > rev_num2:
#     print(f"{num2} < {num1}")
# else:
#     print(f"{num1} = {num2}")
# دریافت ورودی
# k = int(input().strip())

# # محاسبه مجموع زمان لازم برای شارژ از 0 درصد تا k درصد
# total_time = k * (k + 1) // 2

# # چاپ نتیجه
# print(total_time)
# k = int(input().strip())
# total_time = k * (k+1)  // 2
# print(total_time)
# num1 = round(int(input("")))
# slice_in = slice(2,4) 
# print(num1(slice_in))
# # دریافت ورودی
# date_string = input().strip()

# # جدا کردن سال و ماه
# year = date_string[:2]
# month = date_string[2:]

# # چاپ نتیجه
# print(f"saal:{year}")
# print(f"maah:{month}")
# # دریافت ورودی
# m = int(input().strip())

# # لیست کلماتی که با 's' شروع می‌شوند
# s_words = ["sib", "senjed", "somagh", "serke", "sonbol", "sekkeh", "samanoo"]

# # چاپ m کلمه اول از لیست
# for i in range(m):
#     print(s_words[i])
# m = int(input().strip())
# s_words = ["sib","senjed","samagh","serke","sonbol","sekkeh","samanoo"]
# for i in range(m):
#     print(s_words[i])
import networkx as nx
G = nx.Graph()
G.add_edges_from([(1,2),(2,3),(3,4),(4,1)])
path = nx.shortest_path(G,source = 1, target = 3)
print(path)
