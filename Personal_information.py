def solution(today, terms, privacies):
    answer = []
    period = {}
    for i in range(len(terms)):
        Type, month = terms[i].split()
        period[Type] = int(month)

    for i in range(len(privacies)):
        date, useType = privacies[i].split()
        date = list(map(int, date.split('.')))
        date[1] += period[useType]
        if not date[1] % 12:
            date[0] += (date[1]//12)-1
            date[1] = 12
        else:
            date[0] += date[1]//12
            date[1] = date[1] % 12

        canUse = date[0]*10000+date[1]*100+date[2]
        today = today.replace(".", "")
        if canUse <= int(today):
            answer.append(i+1)

    return answer
