def test(firstname,lastname,age):
    print(firstname,lastname,age)

def test1(firstname,lastname="Unknown", age=None):
    print(firstname,lastname,age)

# def test1(firstname,lastname="Unknown", age): #You cant do this default will come at last
    # print(firstname,lastname,age)

test("vimal","lohani",28)
test1("vimal","lohani",28)
test1("vimal")