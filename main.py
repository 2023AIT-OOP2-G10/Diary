from diaries.DiarySample import DiarySample
from diaries.IchikawaDiary import IchikawaDiary
# ↓のリストには、メンバーの各日記が格納されます。 
diaries = [
      DiarySample(),
      IchikawaDiary(),
]

for d in diaries:
      print("---------------------------------")
      print(d.get_date())
      print(d.get_summary())
      print(d.get_author())
      print()