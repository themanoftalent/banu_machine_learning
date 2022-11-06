from datetime import datetime

customers = {
    'name': 'Jack Mann',
     'address': '123 Fake St',
    'age': 23,
    'verification': True

}
for customer in customers.keys():
    print(customer)
print('\n')
print('Customer: ', customers.get('sex'))
print('\n')
print('Customer birthdate: ', customers.get('birth_year','january,1984'))

customers['sex']='male'
print("#####################\nPrinting keys and values for customer")
for key, value in customers.items():
    print(key,':',value)
