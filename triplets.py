N = int(input())
output = []
method =[]
for i in range(0,N):
    method = method.append(input())
    if 'insert' in method[i]:
        ins_met = method[i].split(' ')
        output = output.insert(ins_met[0],ins_met[1])

    elif 'print' in method[i]:
        print(output)
    elif 'remove' in method[i]:
        rem_met = method[i].split(' ')
        output = output.remove(rem_met[1])
    elif 'append' in method[i]:
        app_met = method[i].split(' ')
        output = output.append(app_met[1])
    elif 'sort' in method[i]:
        output = output.sort()
    elif 'pop' in method[i]:
        output = output.pop()
    elif 'reverse' in method[i]:
        output = output.reverse()
