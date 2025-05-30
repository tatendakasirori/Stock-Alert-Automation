
class Stock_change:
    def __init__(self,yesterday:float, db_yesterday:float):
        self.yesterday = yesterday
        self.db_yesterday = db_yesterday
        self.get_percentage_change()

    def get_percentage_change(self):
        self.change = self.yesterday - self.db_yesterday
        self.abs_percentage = abs(self.change/self.yesterday)*100
        if self.change < 0:
            self.percentage_change = f"🔻{round(self.abs_percentage)}%"
        else:
            self.percentage_change = f"🔺{round(self.abs_percentage)}%"