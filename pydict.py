post={'name':'medo','age':'12','friend':'mostafa','phone':(23112441,564634)}
print(type(post))
post2=dict(player="salh",nation="Egypt")
print(post2)
post2["user_fname"]="Mo"
post2["club"]="liverpool"
print(post2)
print(post['name'])
if 'age' in post:
    print(post['age'])
    
else:
    print("key error")
try:
    print(post['loc'])

except KeyError:
    print("the key is unknown")
print(dir(post))

