import datetime


class Pollen:
    """Domain model Pollen"""

    def __init__(self, red, green, blue):
        self.rgb = {int(red), int(green), int(blue)}
        self.created = datetime.datetime.now()
        print(self.season)

    # def __init__(self, hex):
    #     self.hex = hex
    #     self.season = self.get_season()

    @property
    def season(self):
        year_day = self.created.timetuple().tm_yday

        if year_day < 61:
            return 'winter'
        elif year_day < 173:
            return 'spring'
        elif year_day < 265:
            return 'summer'
        elif year_day < 356:
            return 'autumn'
        else:
            return 'winter'
