response_code = 300
match response_code:
    case int():
        if response_code > 99 and response_code < 500:
            print('response code is a valid number')
    case _:
        print('Code is an invalid number')
        
        
spam = 0
while spam < 5:
    print('Hello, world')
    spam = spam + 1                
    
