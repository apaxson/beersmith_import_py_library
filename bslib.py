import xmltodict

class Recipe(object):
    def __init__(self):
        self.rawdata = None
        self.name = None
        self.brewer = None
        self.version = 0
        self.batchsize = 0
        self.fermentables = []
        self.miscs = []
        self.yeasts = []
        self.stylename = None
        self.stylecat = None
        self.stylecatnum = None
        self.styleletter = None
        self.styleguide = None
        self.styletype = None
        self.estabv = 0
        self.calories = 0
        self.date = None
        self.estog = 0
        self.estfg = 0

    def parse(self,file):
        f = open(file, 'rb')
        self.rawdata = xmltodict.parse(f)
        f.close()

        if len(self.rawdata['RECIPES']) > 1:
            raise RuntimeError("Expected 1 recipe, but received " + str(len(self.rawdata['RECIPES'])))

        __recipe = self.rawdata['RECIPES']['RECIPE']
        self.name = __recipe['NAME']
        self.brewer = __recipe['BREWER']
        self.version = __recipe['VERSION']
        self.batchsize = __recipe['BATCH_SIZE']
        self.fermentables = __recipe['FERMENTABLES']
        self.miscs = __recipe['MISCS']
        self.yeasts = __recipe['YEASTS']
        __style = __recipe['STYLE']
        self.stylename = __style['NAME']
        self.stylecat = __style['CATEGORY']
        self.stylecatnum = __style['CATEGORY_NUMBER']
        self.styleletter = __style['STYLE_LETTER']
        self.styleguide = __style['STYLE_GUIDE']
        self.styletype = __style['TYPE']
        self.estabv = __recipe['EST_ABV']
        self.estog = __recipe['EST_OG']
        self.estfg = __recipe['EST_FG']