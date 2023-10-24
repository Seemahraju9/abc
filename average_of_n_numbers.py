def average(*args: int)->float:
    #this validation must be added to avoid zero division error.
    if len(args) == 0:
        raise BaseException
        
    average = 0.0;
    for i in range(len(args)):
        average += args[i]

    average = average/len(args)
    '''Instead of summing using for loop we can use sum function
    average = sum(args)/len(args) '''
    return average

print('''    ___     _______ ____      _    ____ ___ _   _  ____ 
   / \ \   / / ____|  _ \    / \  / ___|_ _| \ | |/ ___|
  / _ \ \ / /|  _| | |_) |  / _ \| |  _ | ||  \| | |  _ 
 / ___ \ V / | |___|  _ <  / ___ \ |_| || || |\  | |_| |
/_/  _\_\_/_ |_____|_|_\_\/_/__ \_\____|___|_| \_|\____|
| \ | | | | |  \/  | __ )| ____|  _ \/ ___|             
|  \| | | | | |\/| |  _ \|  _| | |_) \___ \             
| |\  | |_| | |  | | |_) | |___|  _ < ___) |            
|_| \_|\___/|_|  |_|____/|_____|_| \_\____/  ''')

numbers = []
while (1):
    num = input('Enter a number. Give * to exit\n')

    if (num == '*' || len(num) == 0):
        break
    
    numbers.append(float(num))


print("The average of numbers " ,*numbers, " is ", average(*numbers))   
