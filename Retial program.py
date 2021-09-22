import Retail_class

Item1Price = input('what is the price for item 1?: $')
Item2Price = input('what is the price for item 2?: $')
Item3price = input('What is the price for item 3?: $')
item1units = input('how many units for item 1?: ')
item2units = input('how many units for item 2?: ')
item3units = input('what is the price for item 3?: ')
item1des = input('please enter a description for item 1')
item2des = input('Please enter a description for item 2')
item3des = input('please enter a description for item 3')
item1 = Retail_class.RetailItem(item1des,item1units,Item1Price)
item2 = Retail_class.RetailItem(item2des,item2units,Item2Price)
item3 = Retail_class.RetailItem(item3des,item3units,Item3price)
itemlist = [item1,item2,item3]
print('item summary')

print('Item1')
print('price: $',item1.get_price(),' ','units:',item1.get_units(),'description:',item1.get_description(),)
