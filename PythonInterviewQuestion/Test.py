string="a4b3c2"
output=""
previous=""
for x in string:
    if x.isalpha():
        output+=x
        previous=x
    else:
        output+=previous*(int(x)-1)
print(output)