import pybase64
def im(image):
    img = open(r'C:\Users\User\Pictures\tom and jerry.jpg', 'rb')
    data=pybase64.b64decode(img.read())
    print(data)
    return data
