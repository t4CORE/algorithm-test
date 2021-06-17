def hello(name="persone"):
    print ('Brave new world ' + name)

hello('pink')
hello('floyd')
hello()
hello('alan parson')

def add(numberone, numbertwo):
    return numberone + numbertwo

print(add(10, 40))
print(add(100, 120))

add = lambda numberone, numbertwo: numberone + numbertwo
print(add(10, 35))
