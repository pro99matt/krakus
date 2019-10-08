import urllib

class FileDownlod(object):

    def download(self):

        urllib.urlretrieve('https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/terminowe/synop/2019/'
        , 'data/datas')
