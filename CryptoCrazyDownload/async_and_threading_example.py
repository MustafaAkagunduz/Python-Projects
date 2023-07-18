import threading
import requests
import time as timer
import asyncio
import aiohttp

#application in main.py (and the below get_data_sync func) was synchronous (Fulfills the 10 requests sequentially)

urls = ["https://postman-echo.com/delay/3"] * 10

def get_data_sync(urls): #synchronous
    start_time = timer.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())
    end_time = timer.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
    return json_array
#######################################################


class ThreadingDownloader(threading.Thread): #inheritated

    json_array = []

    def __init__(self,url):
        super().__init__()
        self.url= url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return self.json_array

def get_data_threading(urls):
    start_time = timer.time() #number of threads will be number of URLs
    threads_list = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start() #launches the "run" func.
        threads_list.append(t)

    for x in threads_list:
        x.join() #waits until the thread terminates
        #print(x) #prints the thread

    end_time = timer.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
############################################################

async def get_data_async_but_as_wrapper (urls):
    st = timer.time()
    json_array = []

    async with aiohttp.ClientSession() as session: #these following 3 lines can be used everywhere
        for url in urls:
            async with session.get(url) as resp:
                json_array.append(await resp.json())

    et = timer.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, " seconds")
    return json_array
#######################################################

async def get_data(session, url, json_array):
    async with session.get (url) as resp:
        json_array.append(await resp.json())

async def get_data_async_concurrently (urls) :
    st = timer.time ()
    json_array = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future (get_data(session,url,json_array))) #create_task can be used
        await asyncio.gather(*tasks)


    et = timer.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, " seconds")

    return json_array

#######################################################


#get_data_sync(urls) #approximately 40 secs
#get_data_threading(urls) #approximately 4 secs
#asyncio.run(get_data_async_but_as_wrapper(urls))
#asyncio.run(get_data_async_concurrently(urls))


