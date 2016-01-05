import re
import os

str = "/www/Front/Front.PC.Online/src/ResVacationOnline/js/vacation/app/detail/v_detail.js"
str2 = "D:\git\Tour\Front\Front.PC.Online\src\ResVacationOnline\js\vacation\app\detail\v_detail.js"
# pattern = re.compile('app/detail')
# pattern2 = re.compile(r'\w*.js$')
# match = pattern.search(str)
# match2 = pattern2.search(str)
# if match:
#   print match.group()
# if match2:
#   print match2.group()

# fold = {
#   "detail": "v_detail.js",
#   "order": "pgk_book_fill_next.js"
# }

# for key in fold:
#   pattern = re.compile(key)
#   match = pattern.search(str2)
#   if match:
#     print fold[key]

# str2.split("\\")
# print(str2)

lists = ['abc','def']
print(lists.index('sss'))