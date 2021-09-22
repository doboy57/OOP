import Retail_class

Item1Price = '59.95'
Item2Price = '34.95'
Item3price = '24.95'
item1units = '12'
item2units = '40'
item3units = '20'
item1des = 'jacket'
item2des = 'Designer jeans'
item3des = 'shirt'
item1 = Retail_class.RetailItem(item1des,item1units,Item1Price)
item2 = Retail_class.RetailItem(item2des,item2units,Item2Price)
item3 = Retail_class.RetailItem(item3des,item3units,Item3price)
itemlist = [item1,item2,item3]
print('item summary')

print('Item1')
print('price: $',item1.get_price(),' ','units:',item1.get_units(),'description:',item1.get_description(),)
print('Item2')
print('price: $',item2.get_price(),' units:',item2.get_units(),'description:',item2.get_description(),)
print('Item3')
print('price: $',item3.get_price(),'units:',item3.get_units(),'description:',item3.get_description(),)
