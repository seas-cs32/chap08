### chap08/ale04.py

# A list of messy, complete street addresses and the expected,
# coarsened equivalents. Your task is to complete the function
# `coarsen` so that it produces the second string from the
# first using only bitwise operations, and the built-in
# functions `ord` and `chr`.
addrs = [
    ("119 Reed St", "000 Reed St"),
    ("253 Rindge St", "000 Rindge St"),
    ("6 Emmons Pl", "0 Emmons Pl"),
    ("   113 Walker St", "000 Walker St"),
    ("109 Walker St      ", "000 Walker St"),
    (" 30 Clay St  ", "00 Clay St"),
    ("\t  40 Montgomery St", "00 Montgomery St"),
]

def coarsen(full_addr):
    '''Given a messy full street address return a clean coarsened one'''
    coarsened_addr = ''
    for c in full_addr.strip():
        if c.isnumeric():
            pass
        else:
            coarsened_addr += c

    return coarsened_addr

def main():
    "Driver that tests your function."

    for full_addr, coarsened_addr in addrs:
        r = coarsen(full_addr)
        if r == coarsened_addr:
            print(f'PASSED on test: "{full_addr}"')
        else:
            print(f'FAILED on "{full_addr}", returned:\n\t"{r}"')

if __name__ == "__main__":
    main()
