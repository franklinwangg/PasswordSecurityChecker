import requests
import hashlib

def generate_potential_password_list(password) :
    passwordHash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper() #FIGURE THIS OUT TOMORROW
    first5 = str(passwordHash)[:5]
    response = requests.get('https://api.pwnedpasswords.com/range/' + first5)
    return response

def isolate_password(password) :
    passwordHash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper() #FIGURE THIS OUT TOMORROW
    restOfHash = passwordHash[5:]
    passwordsParagraph = generate_potential_password_list(password).text
    passwordsCount = passwordsParagraph.splitlines()

    for x in passwordsCount :
        if(restOfHash in x) :
            indexOfColon = x.find(":")
            count = x[(indexOfColon + 1) :]
            return count

    print("your password has been unhacked")

print(isolate_password("password123"))