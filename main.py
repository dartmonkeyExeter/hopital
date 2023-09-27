priorityQueue = []
normalQueue = []
while True:
    callOrQueue = str(input('do you want to (c)all the next patient, (a)dd a patient, (r)emove a patient?'))
    if callOrQueue == 'c':
        if priorityQueue:
            print(f'the next patient is from the priority queue and is {priorityQueue[0]}')
            priorityQueue.pop(0)
        elif normalQueue:
            print(f'the next patient is from the normal queue and is {normalQueue[0]}')
        else:
            print('no patients in either queue')
    elif callOrQueue == 'a':
        nameToAdd = str(input('name to add'))
        while True:
            priorityOrNormal = str(input('should they be added to (p)riority or (n)ormal queue'))
            if priorityOrNormal == 'p':
                priorityQueue.append(nameToAdd.lower())
                break
            elif priorityOrNormal == 'n':
                normalQueue.append(nameToAdd.lower())
                break
            else:
                print("invalid input try again")
    elif callOrQueue == 'r':
        whom = str(input(f'who to remove\npriority: {priorityQueue}\nnormal: {normalQueue}'))
        count = 0
        if whom in priorityQueue:
            for i in priorityQueue:
                count += 1
                if i == whom:
                    priorityQueue.pop(count - 1)
        count = 0
        if whom in normalQueue:
            for i in normalQueue:
                count += 1
                if i == whom:
                    normalQueue.pop(count - 1)
    elif callOrQueue == 'clear':
        priorityQueue = []
        normalQueue = []
        print('queues cleared')
    else:
        print('invalid input')
