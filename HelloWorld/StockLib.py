import urllib.request

class Stock:
	"""docstring for Stock"""
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

	def show(self):
		print(self.__code+":"+self.__name+",当前价格："+self.__price)

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

dao = StockDao()
code = 'sz000503'
stock = dao.getStock(code)
stock.show()

#print(resp.geturl())
#print(resp.info())

