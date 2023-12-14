from diaries.AbstractDiary import AbstractDiary
class IchikawaDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"
    def get_summary(self):
        return """今日は初めてのグループワークだった。
途中眠たくなって危なかった。寝てたせいで迷惑かけるのは避けたい。"""
    def get_author(self):
        return "Nagatani"