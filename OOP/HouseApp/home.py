#_*_ encoding:utf-8 _*_

def get_valid_input(input_string, valid_options):
	"""验证输入是否正确"""
	input_string += "({})".format(",".join(valid_options))
	response = input(input_string)
	while response.lower() not in valid_options:
		response = input(input_string)
	return response


class Property(object):
	"""基类，其他子类继承于此"""
	def __init__(self, square_feet = '', beds = '', baths = '', **kwargs):
		super().__init__(**kwargs)   #消费”关键字“避免我们的super().__init__方法在多重继承链中不是最后一个调用
		self.square_feet = square_feet #房产面积
		self.num_bedrooms = beds #房产卧室的数量
		self.num_baths = baths #房产中浴室的数量

	def dispaly(self):
		"""打印房产细节"""
		print("属性细节")
		print("="*10)
		print("房产面积：{}".format(self.square_feet))
		print("卧室数量：{}".format(self.num_bedrooms))
		print("浴室数量：{}".format(self.num_baths))
		print("="*10)

	def prompt_init():
		"""用字典存储__init__方法的值"""
		return dict(square_feet = input("输入房产面积："),
		            beds = input("输入卧室数："),
		            baths = input("输入浴室数："))
	#创建prompt__init的静态方法
	prompt_init = staticmethod(prompt_init)

class Apartment(Property):
	"""公寓类，继承Property"""
	valid_laundries = ('coin', 'ensuite', 'none')#洗衣房
	valid_balconies = ('yes', 'no', 'solarium')#是否有阳台

	def __init__(self, balcony = '', lanundry = '', **kwargs):
		super().__init__(**kwargs)
		self.balcony = balcony  #洗涤方式
		self.lanundry = lanundry   #阳台


	def display(self):
		super().dispaly()
		print("公寓细节")
		print("lanundry:%s"%self.lanundry)
		print("是否有阳台：%s"%self.balcony)


	def prompt_init():
		parent_init= Property.prompt_init()
		lanundry = get_valid_input("拥有什么类型的laundry?"
		                           "类型有?",
		                           Apartment.valid_laundries)
		balcony = get_valid_input("公寓有阳台吗?",
		                           Apartment.valid_balconies)
		parent_init.update({
		    "balcony":balcony,
		    "lanundry":lanundry
		})
		return parent_init
	prompt_init = staticmethod(prompt_init)


class House(Property):
	valid_garage = ('attached', 'detached', 'none') #车库类型（连接的，分离的，没有）
	valid_fenced = ('yes', 'no')#围墙 	

	def __init__(self, num_stories='', garage='', fenced='', **kwargs):
		super().__init__(**kwargs)
		self.garage = garage
		self.fenced = fenced
		self.num_stories = num_stories #仓库数量

	def display(self):
		super().dispaly()
		print("房子属性细节")
		print("仓库数量：{}".format(self.num_stories))
		print("车库：{}".format(self.garage))
		print("是否有围墙：{}".format(self.fenced))

	def prompt_init():
		parent_init = Property.prompt_init()
		fenced = get_valid_input("院子有围墙吗？",House.valid_fenced)
		garage = get_valid_input("房子有车库吗？",House.valid_garage)
		num_stories = input("房子有多少仓库？")
		parent_init.update({
		    "fenced":fenced,
		    "garage":garage,
		    "num_stories":num_stories
		})
		return parent_init
	prompt_init = staticmethod(prompt_init)


class Purchase():
	"""买房"""
	def __init__(self, price='', taxes='', **kwargs):
		super().__init__(**kwargs)
		print("购买细节")
		print("出售价格：{}".format(self.price))
		print("缴纳税款：{}".format(self.taxes))

	def prompt_init():
		return dict(
		    price = input("出售价格是多少？"),
		    taxes = input("需要缴纳的税款为？"))
	prompt_init = staticmethod(prompt_init)


class Rental(object):
	"""租房"""
	def __init__(self, furnished='', utilities='', rent='', **kwargs):
		super().__init__(**kwargs)
		self.furnished = furnished
		self.utilities = utilities
		self.rent = rent


	def display(self):
		super().dispaly()
		print("租房细节")
		print("房租（/月）：{}".format(self.rent))
		print("是否有家具：{}".format(self.furnished))
		print("是否有公共设施：{}".format(self.utilities))

	def prompt_init():
		return dict(
		    rent = input("请输入每个月的房租："),
		    utilities = input("是否有公共设施？"),
		    furnished = get_valid_input("是否安装了家具？",("yes","no"))
		    )
	prompt_init = staticmethod(prompt_init)

class HouseRental(Rental, House):
	def prompt_init():
		init = House.prompt_init()
		init.update(Rental.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
	def prompt_init():
		init = Apartment.prompt_init()
		init.update(Rental.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
	def prompt_init():
		init = Apartment.prompt_init()
		init.update(Purchase.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase, House):
	def prompt_init():
		init = House.prompt_init()
		init.update(Purchase.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)


class Agent(object):
	
	def __init__(self):
		self.property_list = []
		self.type_map = {
			("house", "rental"):HouseRental,
			("house", "purchase"):HousePurchase,
			("apartment", "rental"):ApartmentRental,
			("apartment", "purchase"):ApartmentPurchase
			}	

	def display_properities(self):
		for property in self.property_list:
			property.dispaly() 

	def add_property(self):
		property_type = get_valid_input(
		    "房子的类型：",
		    ("house", "apartment")).lower()
		payment_type = get_valid_input(
		    "租房还是买房？",
		    ("purchase", "rental")).lower()


		PropertyClass = self.type_map[
			(property_type, payment_type)]
		init_args = PropertyClass.prompt_init()
		self.property_list.append(PropertyClass(**init_args))
		    



















































