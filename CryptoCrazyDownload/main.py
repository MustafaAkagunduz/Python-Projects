#(url="https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")

#post,put,delete,get are important

##following are methods of communicating the server. -> get vs post

import requests as rq

response = rq.get(url="https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
def get_crypto_data():
    if response.status_code == 200:
        return response.json()
    '''#prints the requested text
    #print(response.text)'''
    #or print(response.json())
    '''
    for crypto in response.json():
        print(crypto["currency"])

    '''

    '''
    print("success")
else:
    print("unsuccess access")
print(response)
print(response.status_code)
'''

crypto_response = get_crypto_data()
user_input = input("Enter your crypto currency: ")

for crypto in crypto_response:
    if crypto["currency"] == user_input:
        print(crypto["price"])
        break
