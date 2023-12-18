from diaries.DiarySample import DiarySample
from diaries.KoukiDiary import DiaryKouki
from diaries.NakagawaDiary import DiaryNakagawa
from diaries.satosomaDiary import Diarysatou
from diaries.furutaDiary import Diaryfuruta
from diaries.ShintaroDaiary import DiaryShintaro
from diaries.shionDiary import Diaryshion
from diaries.IchikawaDiary import Diaryichikawa
from diaries.sekiguchiDiary import Diarysekiguchi
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           DiaryKouki(),
           Diarysatou(),
           Diaryfuruta(),
           Diaryshion(),
           DiaryShintaro(),
           Diaryichikawa(),    
           Diarysekiguchi(),
           DiaryNakagawa(),
           ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()