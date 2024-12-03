def times_in_list(number, list):
    count = 0

    for i in list:
        if i == number:
            count += 1

    return count

def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()

    list1 = []
    list2 = []

    distance = 0
    similarity_score = 0

    for line in lines:
        separated_line = line.split("   ")
        
        list1.append(int(separated_line[0]))
        list2.append(int(separated_line[1]))

    # Ordenar las listas ascendentemente
    list1.sort()
    list2.sort()

    # Calcular la distancia
    for i in range(len(list1)):
        # distance += abs(list1[i] - list2[i])
        score = times_in_list(list1[i], list2)
        score = score * list1[i]
        similarity_score += score

    print(similarity_score)
    #print(distance)

if __name__ == "__main__":
    main()