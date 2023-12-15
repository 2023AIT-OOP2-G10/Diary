from diaries.DiarySample import DiarySample
from diaries.KoukiDiary import DiaryKouki
from diaries.satosomaDiary import Diarysatou
from diaries.furutaDiary import Diaryfuruta
from diaries.ShintaroDaiary import DiaryShintaro
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           DiaryKouki(),
           Diarysatou(),
           Diaryfuruta(),
           DiaryShintaro(),
           ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
