import requests as rq
import json #bir veriyi json'a dönüştürmek veya json'ı bir veriye dönüştürmek için kullanılır
#url = "https://jsonplaceholder.typicode.com/todos" #for the all to-dos
#url2 = "https://jsonplaceholder.typicode.com/todos/2" #brings the second to-do
'''
#brings the input user want:
user_input = input("Enter id: ")
url_input_FOR_GET_REQUEST = f"https://jsonplaceholder.typicode.com/todos/{user_input}" 
'''

#get request: (for bringing data)
#get_response = rq.get(url)
#print(get_response.json())

############################################################################################

#post request (for adding or changing data on DB)
#let's add an new to-do:
'''
prototype:
{
    "userId": 1,
    "id": 1, #auto-incremented task id
    "title": "delectus aut autem",
    "completed": false
  }

'''
to_do_item= {
    "userId": 4152,
    #"id": 1, #auto-incremented task id
    "title": "MY TODO",
    "completed": False
  }
url_str_for_post_request = "https://jsonplaceholder.typicode.com/todos"
#optional header
headers_example = {"Content-Type" : "application/json"}
#post_response = rq.post(url_str_for_post_request, to_do_item,  headers=headers_example)

#eğer veriyi json p.metresi ile değil ille 'data' parametresiyle göndermemiz gerekiyorsa json modülü kullanılır. yukarıda import edildi
# following is used: (json.dumps(to_do_item))
#new_post_response = rq.post(url_str_for_post_request, data=json.dumps(to_do_item),  headers=headers_example)
#print(new_post_response.json())


#executed fine but didn't added the jsonplaceholder DB really, it treats like that :)
#but post request are done in real life just like this way (header may be wanted)


#############################################################################################

#PUT REQUEST: for updating all the fields of the entry from DB
'''
url_for_put_request = "https://jsonplaceholder.typicode.com/todos/15"
to_do_item_15= {
    "userId": 2817,
    #"id": 1, #auto-incremented task id, we don't want it to be changed actually :)
    "title": "PUT TODO",
    "completed": True
  }

put_response = rq.put(url_for_put_request, json = to_do_item_15)
print(put_response.json())
'''
#############################################################################################


#PATCH REQUEST: for updating the single field of the entry from DB
#not used so much :D
'''url_for_patch_request = "https://jsonplaceholder.typicode.com/todos/15"

to_do_item_patch_15= {
    "userId": 2817,
    #"id": 1, #auto-incremented task id, we don't want it to be changed actually :)
    "title": "Patch request test",
    "completed": True
  }

patch_response = rq.patch(url=url_for_patch_request, json=to_do_item_patch_15)
print(patch_response.json())
'''
#############################################################################################


#DELETE REQUEST: for deleting from DB

url_for_delete_request = "https://jsonplaceholder.typicode.com/todos/15"
delete_response = rq.delete(url_for_delete_request)
print(delete_response.json())
print(delete_response.status_code)


#############################################################################################

