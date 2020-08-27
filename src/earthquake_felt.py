import tabulate
from src.base import Base


class EarthquakeFelt(Base):
    def __init__(self):
        Base.__init__(self, "https://data.bmkg.go.id/gempadirasakan.xml")

    def __repr__(self):

        temp = []

        for i in range(len(self.root)):

            self.data.append([i+1, "", ""])

            for j in range(len(self.root[i])):
                tag = self.root[i][j].tag
                text = self.root[i][j].text

                if tag == 'point':
                    temp.extend(
                        [[self.root[i][j][0].tag,
                          "|",
                          self.root[i][j][0].text]])
                    continue

                temp.extend([[tag, "|", text]])
                if len(temp) == 8:
                    self.data.extend(temp)
                    self.data.append(["", "", ""])
                    temp.clear()
                    continue

        self.data.append(["Sumber", ":", "https://data.bmkg.go.id/gempadirasakan.xml"])

        return tabulate.tabulate(self.data, tablefmt="plain")
