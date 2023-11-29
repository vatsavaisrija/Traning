from barcode import Code128


def generate(data):
    code = Code128(data)
    code.save('barcode')
    return code