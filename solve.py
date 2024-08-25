def rev(file):
    with open(file, 'r') as file:
        for line in file:
            line = line.strip()
            hex_bytes = line.split()
            revb = hex_bytes[::-1]
            reversed = ' '.join(revb)
            print(reversed)
file = 'challenge.dat'
rev(file)