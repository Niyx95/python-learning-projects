import random, time, sys

#proxy servers available to the user
cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Toronto",
    "Mexico City",
    "London",
    "Paris",
    "Berlin",
    "Rome",
    "Madrid",
    "Tokyo",
    "Shanghai",
    "Beijing",
    "Mumbai",
    "Seoul",
    "Sydney",
    "Melbourne",
    "São Paulo",
    "Buenos Aires",
    "Rio de Janeiro",
    "Cairo",
    "Lagos",
    "Johannesburg",
    "Dubai",
    "Singapore"
]

choice = input("What server do you wanna connect to? >>\n").title()


#function to connect to a server.
def connect_proxy(server, server_list):

    attempt = 0
    max_retries = 7

    #try except block to catch any errors:
    try:
            #check if server is in the server list
            if server not in server_list:
                print(f'Error: {server} is not in the proxy server list.')
                return
            #trying to connect to server
            while attempt < max_retries:
                attempt += 1
                if random.choice([True, False, False, False, True, False]):
                    print(f'trying to connect to: {server}')
                    time.sleep(0.5)

            print(f'Successfully connected to: {server}')

    #if user interrupt do this:
    except KeyboardInterrupt:
        print("Connection canceled. Quitting....")
        sys.exit()

connect_proxy(choice, cities)
