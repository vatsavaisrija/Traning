x=open('demo.txt' , mode='w+')
x.write(" w+ mode")
x.seek(0)
print(x.read())
x.close()


x=open('demo.txt' , mode='r')
print(x.read())
x.close()

x=open('demo.txt' , mode='w')
x.write("Have a great time")
x.close()

x=open('demo.txt' , mode='a')
x.write("Have a great time")
x.close()

x=open('demo.txt' , mode='r+')
print(x.read())
x.write(" r+ mode")
x.close()