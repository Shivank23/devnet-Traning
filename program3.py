import json
data_JSON ="""
{
	"size": "Medium",
	"price": 15.67,
	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
	"client": {
		"name": "Jane Doe",
		"phone": "455-344-234",
		"email": "janedoe@email.com"
	}
}""" 
print(type(data_JSON))

dict_data=json.loads(data_JSON)  #convert json into dict
print(dict_data)
print(type(dict_data))