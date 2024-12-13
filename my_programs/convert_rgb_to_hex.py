from webcolors import name_to_hex

def color_name_to_code(color_name):
    try:
        color_code = name_to_hex(color_name)
        return color_code
    except ValueError:
        return None
    
color_name = input('Informe o nome da cor: ')
result_code = color_name_to_code(color_name)

print(f'\nA cor em valor hexadecimal: {result_code}')