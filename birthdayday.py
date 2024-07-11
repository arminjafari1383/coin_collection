# دریافت ورودی
date_string = input().strip()

# جدا کردن سال و ماه
year = date_string[:2]
month = date_string[2:]

# چاپ نتیجه
print(f"saal:{year}")
print(f"maah:{month}")