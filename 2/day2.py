def lista_ordenada(lista, limit = 3):
    lista = [int(i) for i in lista]

    # Verifica si está ordenada ascendentemente con el límite
    ascendent = all(abs(lista[i] - lista[i + 1]) <= limit and lista[i] < lista[i + 1] for i in range(len(lista) - 1))
    
    # Verifica si está ordenada descendentemente con el límite
    descendent = all(abs(lista[i] - lista[i + 1]) <= limit and lista[i] > lista[i + 1] for i in range(len(lista) - 1))

    return ascendent or descendent

def probar_eliminacion(lista):
    for i in range(len(lista)):
        copia = lista[:i] + lista[i + 1:]
        if lista_ordenada(copia):
            return True

    return False


def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()

    safe_reports = 0

    for line in lines:
        line = line.split()
        
        valor = lista_ordenada(line)

        if valor:
            safe_reports += 1
        else:
            posible = probar_eliminacion(line)
            if posible:
                safe_reports += 1

    print(safe_reports)

if __name__ == "__main__":
    main()