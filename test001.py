def is_jumping(number):
    # write your code here
    if number == 0:
        return "JUMPING"
    
    if number and int(number) >= 0:
        num_str = str(number)

        if len(num_str) == 1:
            return "JUMPING"
        
        for i in range(1, len(num_str)):
            current_num = int(num_str[i])
            prev_num = int(num_str[i-1])
            if abs(current_num - prev_num) != 1:
                return "NOT JUMPING"
        
        return "JUMPING" 
   
print(is_jumping(4))
print(is_jumping(0))
print(is_jumping(44))
print(is_jumping(123456))
print(is_jumping(2345432))
print(is_jumping(445678))
print(is_jumping(4567899))
print(is_jumping(4815))