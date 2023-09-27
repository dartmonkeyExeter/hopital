priorityQueue = []
normalQueue = []
priorityDoctor = []
normalDoctor = []


def call_next_patient():
    if priorityQueue:
        print \
            (f'the next patient is from the priority queue and is {priorityQueue[0]} and their Doctor is {priorityDoctor[0]}')
        priorityQueue.pop(0)
        priorityDoctor.pop(0)
    elif normalQueue:
        print \
            (f'the next patient is from the normal queue and is {normalQueue[0]} and their Doctor is {normalDoctor[0]}')
        normalQueue.pop(0)
        normalDoctor.pop(0)
    else:
        print('no patients in either queue')


def add_patient():
    nameToAdd = str(input('name to add\n'))
    while True: 
        priorityOrNormal = str(input('should they be added to (p)riority or (n)ormal queue?\n'))
        if priorityOrNormal == 'p':
            doctorName = str(input('what doctor should they be with?\n'))
            priorityQueue.append(nameToAdd.lower())
            priorityDoctor.append(doctorName)
            break
        elif priorityOrNormal == 'n':
            doctorName = str(input('what doctor should they be with?\n'))
            normalQueue.append(nameToAdd.lower())
            normalDoctor.append(doctorName)
            break
        else:
            print("invalid input try again")


def remove_patient():
    s = ', '
    p = s.join(priorityQueue)
    n = s.join(normalQueue) # this and the prior two lines just make it look nicer when printed
    whom = str(input(f'who to remove\npriority: {p}\nnormal: {n}\n'))
    count = 0
    if whom in priorityQueue:
        for i in priorityQueue:
            count += 1
            if i == whom:
                priorityDoctor.pop(count - 1)
                priorityQueue.pop(count - 1)
    count = 0
    if whom in normalQueue:
        for i in normalQueue:
            count += 1
            if i == whom:
                normalDoctor.pop(count - 1)
                priorityQueue.pop(count - 1)
    print('if the person was found in either queue, they have been removed.')


def main(priorityQueue, normalQueue, priorityDoctor, normalDoctor):
    while True:
        callOrQueue = str(input('do you want to (c)all the next patient, (a)dd a patient, (r)emove a patient? type '
                                'clear to clear both queues.\n'))
        if callOrQueue == 'c':
            call_next_patient()
        elif callOrQueue == 'a':
            add_patient()
        elif callOrQueue == 'r':
            remove_patient()
        elif callOrQueue == 'clear':
            priorityQueue = []
            normalQueue = []
            priorityDoctor = []
            normalDoctor = []
            print('queues cleared')
        else:
            print('invalid input')


if __name__ == '__main__':
    main(priorityQueue, normalQueue, priorityDoctor, normalDoctor)
