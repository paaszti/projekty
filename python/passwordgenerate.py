def password_generator():
    import random
    passwords=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','v','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','$','%',"^",'&','*']
    x=int(input("How long should be your password? "))
    password=[]
    for user in range (0, x):
        password.append(random.choice(passwords))
        password2 = "".join(password)
    print(password2)
password_generator()
