def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()

    safe_reports = 0

    for line in lines:
        decreasing = False
        increasing = False

        # Separamos las líneas
        line = line.split(" ")
        line = [int(i) for i in line]

        # Evalúo el primer índice
        if line[1] < line[0] and (line[0] - line[1]) <= 3:
            decreasing = True
        elif line[1] > line[0] and (line[1] - line[0] <= 3):
            increasing = True
        else:
            continue

        for i in range(1, len(line) - 1):
            if line[i+1] < line[i] and (line[i] - line[i+1]) <= 3 and decreasing:
                decreasing = True
            elif line[i+1] > line[i] and (line[i+1] - line[i]) <= 3 and increasing:
                increasing = True
            else:
                safe_reports -= 1
                break
            
        safe_reports += 1

    print(safe_reports)

if __name__ == "__main__":
    main()