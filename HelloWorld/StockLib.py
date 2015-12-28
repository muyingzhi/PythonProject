import urllib.request

class Stock:
	"Stock,股票数据分析，来自sina财经"
	__name = ""
	__code = ""
	__price= 0
	__list = ""
	def __init__(self, code, dataList):
		super(Stock, self).__init__()
		self.__list = dataList
		self.__name = dataList[0]
		self.__code = code
		self.__price= dataList[3]

	def __str__(self):
		return (self.__code+":"+self.__name+",当前价："+self.__price)

class StockDao:
	"""docstring for StockDao"""
	def __init__(self):
		super(StockDao, self).__init__()

	def getStock(self, code ):
		url = 'http://hq.sinajs.cn/list='+ code
		resp =urllib.request.urlopen(url)


		html = str(resp.read().decode("GBK"))
		tmp = html.split("=")
		values = tmp[1].replace('"','').replace(";",'').split(",")
		stock = Stock(code, values)
		return stock
def readStock(code):
	dao = StockDao()
	stock = dao.getStock(code)
	return stock
#print(resp.geturl())
#print(resp.info())

