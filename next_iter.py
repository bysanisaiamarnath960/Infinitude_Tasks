class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line.rstrip('\n')
        else:
            self.file.close()
            raise StopIteration
        

obj= FileReader('weekday.csv')
for line in obj:
    try:
        print(line)
    except Exception as e:
        print(f"the error occured: {e}")
    

