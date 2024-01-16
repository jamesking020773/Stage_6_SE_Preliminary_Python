def login_required(func):

    def wrapper(): 
        if user_is_logged_in:  # Check if the user is logged in
            return func()  # Call the function if the user is logged in
        else:
            raise Exception("User is not logged in.")  # Raise an exception or handle it with another function
    return wrapper  # Return the wrapper function

@login_required
def some_secure_function(): # Function that requires the user to be logged in. Applying the @login_required decorator means this function will only execute if the user is logged in.
    print("Access granted to the secure function.")

user_is_logged_in = False  # Set this to False to test the unauthorized access

some_secure_function()  # This will either run the function or raise an exception based on the login status