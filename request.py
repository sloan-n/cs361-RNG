import client

def request():

    while True:
        # Get user request
        run = input("Enter 1 for random number or 0 to exit: ")

        # If request to client is 1, get random integer from server
        if run == "1":
            randomInt = client.client()
            print(randomInt)
        
        # If request is 0, exit program
        elif run == "0":
            break
        else:
            print("Sorry invalid input, try again...")



if __name__ == '__main__':
    request()