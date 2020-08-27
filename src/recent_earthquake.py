import tabulate
from .base import Base


class RecentEarthquake(Base):
    def __init__(self):
        Base.__init__(self, "https://data.bmkg.go.id/autogempa.xml")

    def __repr__(self):

        for i in range(len(self.root[0])):
            if self.root[0][i].tag == 'point':
                self.data.extend(
                    [[self.root[0][i][0].tag,
                      "|",
                      self.root[0][i][0].text]])
                continue
            self.data.extend([[self.root[0][i].tag,
                               "|",
                               self.root[0][i].text]])

        self.data.append(["Sumber", "|", "https://data.bmkg.go.id/autogempa.xml"])

        return tabulate.tabulate(self.data, tablefmt="simple")