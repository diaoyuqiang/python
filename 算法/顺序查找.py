# list = ["01", "02", "03"]

def linear_search(li, var):
    for ind, v in enumerate(li):
        if v == var:
            return ind
    else:
        return None

# result = linear_search(list, "02")
# print(result)

