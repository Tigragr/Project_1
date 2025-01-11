
def file_matrix() ->list:
    with open('Bookroom.txt', 'r', encoding = 'utf-8') as file:
        file_var = file.read()
    return [el.split(";") for el in file_var.split('\n')]

def add_to_file(new_note: str) ->None:
    with open('Bookroom.txt', 'a', encoding = 'utf-8') as file:
        file.write(new_note)

def file_rewrite(str_for_rewr: str) ->None:
    with open('Bookroom.txt', 'w', encoding = 'utf-8') as file:
        file.write(str_for_rewr)