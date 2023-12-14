from diaries.AbstractDiary import AbstractDiary


class Diarysatou(AbstractDiary):
    def get_date(self):
        return "2021-12-14"

    def get_summary(self):
        return "疲れた"

    def get_author(self):
        return "佐藤壮真"
