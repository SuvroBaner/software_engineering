'''
    Making asynchronous HTTP Requests to make a non-blocking code.

    Asynchronous routines are able to pause while waiting on their ultimate result to let other routines run in the meantime.
    So, asynchornous code through above mechanism facilitates concurrent execution. It doesn't "block" other code from running so we call it as "non-blocking" code.

    HTTP requests are a classic example of something that is well-suited to asynchronicity because they involve waiting for a response from a server, during
    which time it would be convinient and efficient to have other code running.

    Here, we will run both asynchronous HTTP request using aiohttp and synchronous HTTP request using requests library and compare.
'''

# pip install aiohttp==3.7.4.post0
# pip install requests==2.25.1


# We will use the GET request to get the data from Pokemon API

# import asyncio
# from time import time
# import aiohttp

# async def main():
    
#     async with aiohttp.ClientSession() as session:
#         pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
        
#         async with session.get(pokemon_url) as resp:
#             pokemon = await resp.json()
#             print(pokemon['name'])

# asyncio.run(main())

'''
In this code we are creating a coroutine called "main" which are running with asyncio event loop. (You can think of an event loop as something like a 
while True loop that monitors coroutines, taking feedback on what's idle, and looking around for things that can be executed in the meantime.

Here we are opening an aiohttp client session, a single object that can be used for quite a number of individual requests and by default can make connections
with up to 100 different servers at a time. With this session, we are making a request to the Pokemon API and then waiting a response.

This async keyword basically tells the Python interpreter that the couroutine we are defining should be run asynchronously with an event loop.
The await keyword passes control back to the event loop, suspending the execution of the surrounding coroutine and letting the event loop run other things 
until the result that is being awaited is returned.
'''

'''
Making large number of requests
'''

# import aiohttp
# import asyncio
# import time

# start_time = time.time()

# async def main():

#     async with aiohttp.ClientSession() as session:

#         # all 150 of the original Pokemon
#         for number in range(1, 151):
#             pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
#             async with session.get(pokemon_url) as resp:
#                 pokemon = await resp.json()
#                 print(pokemon['name'])

# asyncio.run(main())
# print("---- %s seconds ---" % (time.time() - start_time))


'''
   It takes 28.33 seconds
   Let's compare with the synchronous execution of the HTTP request using requests library.

'''

# import requests
# import time

# start_time = time.time()

# for number in range(1, 151):
#     url = f'https://pokeapi.co/api/v2/pokemon/{number}'
#     resp = requests.get(url)
#     pokemon = resp.json()
#     print(pokemon['name'])

# print("---- %s seconds---" % (time.time() - start_time))

'''
For each consecutive request, we have to wait for the previous step to finish before even beginning the process. 
It takes much longer because this code is waiting for 150 requests to finish sequentially
It takes : 78.28 secs
'''

'''
Utilizing asyncio for improved performance

In the original example, we are using "await" after each individual HTTP request, which isn't quite ideal.
It is still faster than the requests example because we are running everything in coroutines.

Instead we can run all these requests "concurrently" as asyncio tasks and then check the results at the end, using 
asyncio.ensure_future as asyncio.gather

This is how it will work. If the code that actually makes the request is broken out into own coroutine function, we can create a list of tasks,
consisting of futures for each request. We can then unpack this list to a gather call, which runs them all together.
When we "await" this call to asyncio.gather, we will get back an iterable for all of the futures that were passed in, maintaining their order in the list.
This way we are only awaiting one time
'''

import aiohttp
import asyncio
import time

start_time = time.time()

async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']

async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)


asyncio.run(main())
print("--- %s seconds --- " % (time.time() - start_time))

'''
    This takes 1.17 seconds. This example is completely non-blocking. so the total time to run all 150 requests is going to be roughly equal to the amount of 
    time that the longest request took to run.
'''

