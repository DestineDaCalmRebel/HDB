
#def open_file():
    #with open(r'Nutrients\Calcium\id_calcium.txt', "r") as f:
        #return f.read()


def file_search(neut):
    with open(f'Nutrients/{neut}/id_{neut}.txt', "r") as f:
            return f.read().strip()



