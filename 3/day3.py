import re

def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()

    patron = r'mul\((\d+),(\d+)\)'

    resultados = re.findall(patron, lines[0])
    total = 0

    for line in lines:
        resultados = re.findall(patron, line)

        for resultado in resultados:
            total += int(resultado[0]) * int(resultado[1])

    print(total)

if __name__ == "__main__":
    main()