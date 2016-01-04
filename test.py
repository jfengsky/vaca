import re

str = "/www/Front/Front.PC.Online/src/ResVacationOnline/js/vacation/app/detail/v_detail.js"
# pattern = re.compile('app/detail')
# pattern2 = re.compile(r'\w*.js$')
# match = pattern.search(str)
# match2 = pattern2.search(str)
# if match:
#   print match.group()
# if match2:
#   print match2.group()

fold = {
  "app/detail": "v_detail.js",
  "app/order": "pgk_book_fill_next.js"
}

for key in fold:
  pattern = re.compile(key)
  match = pattern.search(str)
  if match:
    print fold[key]