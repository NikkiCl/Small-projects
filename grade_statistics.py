import math 

def input_from_user():
    list1 = []
    check = ''
    num = " "
    values = []
    while num is not '':
        try:
            num = input("Exam points and exercises completed:").split(" ")
            if num is not check:
                res = [eval(i) for i in num]
                result1 = res[0] + res[1] / 10
                if res[0] < 10:
                    values.append(False)
                else:
                    values.append(True)
                list1.append(math.floor(result1))
        except:
            return list1, values

def statistics(list1 : list, values : list):
    list2 = [0 for x in range(6)]
    for i in range(len(list1)):
        if values[i] == False:
            list1[i] = 0
    for num in list1:
        if num <= 14:
            list2[0] += 1
        elif num <= 17:
            list2[1] += 1
        elif num <= 20:
            list2[2] += 1
        elif num <= 23:
            list2[3] += 1
        elif num <= 27:
            list2[4] += 1
        elif num <= 30:
            list2[5] += 1
    return list2 

def statistics2(list1 : list):
    if len(list1) > 0:
        total = sum(list1)
        result = total / len(list1)
        result = '%.1f' % result
        return result

def statistics3(list2: list):
    perc = 0
    if sum(list2) == 0:
        return f"%.1f"  % perc 
    for i in range(1, len(list2)):
        perc += list2[i]
    perc = perc / sum(list2) * 100
    perc = '%.1f' % perc
    return perc

def printOut(result : float, perc: float, list2 : list):
    print1 = f"""Statistics:
Points average: {result}
Pass percentage: {perc}
Grade distribution: """
    for i in range(5, -1, -1):
        print1 += f"\n  {i}: {list2[i] * "*"}"
    return print1



def main():
    inputd,fae = input_from_user()
    result = printOut(statistics2(inputd),statistics3(statistics(inputd, fae)), statistics(inputd,fae))
    print(result)

if __name__ == "__main__":
    main()
