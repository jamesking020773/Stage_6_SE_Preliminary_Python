def authorised(f):
    def wrapper():
        logged_in = False
        print(f"User Login Status: {logged_in}")
        if (logged_in):
            return f()
        else:
            print("Error: User is not logged in")
    return wrapper

@authorised
def hello(): # Only authorised users should see this message
    print("Hello world!")

hello() # When you call hello, it's wrapped by authorised.
# By placing @authorised above the function definition, it's the same as saying hello = authorised(hello)
