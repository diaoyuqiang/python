def info_format(obj):
    content = {}
    # print(obj.__dict__)
    for item in obj.__dict__:
        key = item.split("__")[-1]
        print(key)
        value = obj.__dict__[item]
        content[key] = value
    return content


class AudioFile:
    def __init__(self):
        self.a = 'dyq'
        self.b = 1234
        self.lis = {"a":1, "b":2}

    def save(self, filename):
        content = info_format(self)
        with open(filename+".txt", "a") as file:
            file.writelines(str(content)+'\n')


au = AudioFile()
au.save('test_save')
