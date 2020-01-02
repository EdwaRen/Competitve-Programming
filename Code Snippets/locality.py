def test_local():
    x = 1
    def inner(x):
        x = 2
    inner(x)
    print(x)

test_local()
# Returns 1


def test_local_list():
    x = [1]
    def inner(x):
        x = [2]
    inner(x)
    print(x)

test_local_list()
# Returns [1]

def test_local_list_action():
    x = [1]
    def inner(x):
        x.append(2)
    inner(x)
    print(x)

test_local_list_action()
# Returns [1, 2]...
