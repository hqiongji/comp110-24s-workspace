def called_function():
    print("Hello from the called function!")
    return "Hello"

def caller_function():
    result = called_function
    print(f"the called function returned: {result}")

caller_function()
    
