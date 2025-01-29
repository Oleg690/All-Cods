loginpassword = input('Introduceti login-ul si parola prin doua puncte: ')

login,password = [],[]

y = loginpassword.split()

for i in y:
    a = i.split(':')
    login.append(a[0])
    password.append(a[1])

print('Login-uri: ',login)
print('Password-uri :',password)