

def my_fun_function(say_this):
    print(say_this)


my_fun_function("hello world")

checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)


def create(item):
    checklist.append(item)


def read(index):
    return checklist[index]


checklist = ['Blue', 'Orange']
checklist[1] = 'Cats'
print(checklist)


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    '''print(read(1))'''

    def list_all_items():
        index = 0
        for list_item in checklist:
            print(str(index) + list_item)
            index += 1
