''' Type hints untuk fungsi '''

# bentuk standar fungsi yang udah kita pelajari


# def fungsi(parameter):
#     hasil = parameter**2
#     print(f"hasil adalah {hasil} \n\n")

# fungsi(1)
# fungsi("Ucup")
# fungsi(True)


# penggunaan type hints

import string

def sepuluh_pangkat(argument:int) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(4.5)
print(f"HASIL adalah {HASIL} \n\n")

def display(argument:string):
    print(f"argument adalah {argument}")

display("Ucup")