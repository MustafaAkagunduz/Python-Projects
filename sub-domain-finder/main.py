import requests as rq

#domain: google.com // subdomain: images.google.com


def make_request(url):
    try:
        return rq.get(url)
    except:
        pass
        #rq.exceptions.ConnectionError()

target_input = input("enter your target website: ")

#open the file
with open("subdomainlist.txt", 'r') as subdomain_list:
    #print(subdomain_list.read()) #returns the content as a stream. won't be used in this project
    for word in subdomain_list:
        word = word.strip() #this built-in function is used for getting rid of unwanted characters.
        #another example: word.strip(",.g") -> deletes the commas,dots and g's in the string
        #useful for url works
        #print(word) we get the content

        url = "https://"+ word + "." + target_input #which website to be tested. this arg is taken from user
        response =make_request(url)

        if response: #means if response isn't None
            print("Found subdomain -> ", url)

