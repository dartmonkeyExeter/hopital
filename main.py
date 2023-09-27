# initialize empty queues and doctor lists
priorityQueue = []
normalQueue = []
priorityDoctor = []
normalDoctor = []
doctors = []

class Doctor:
    def __init__(self, name, queue):
        self.queue = queue
        self.name = name

while True:
    num_doctors = input('how many doctors are here today?\n')
    try:
        num_doctors = int(num_doctors)
        break
    except:
        print('please insert an integer value.')
        continue

for i in range(num_doctors):
    name = input(f"enter the name of doctor {i + 1}: ")
    queue = []
    doctors.append(Doctor(name, queue))

for i, doctor in enumerate(doctors):
    print(f"Doctor {i + 1}: {doctor.name}")




# function to call the next patient
def call_next_patient(doctors):
    while True:
        whichDoctor = input('which doctors queue, please input as interger')
        try:
            whichDoctor = int(whichDoctor)
        except:
            print('write a number')
            continue
        print(f'the next patient in doctor {doctors[whichDoctor - 1].name}s queue is {doctors[whichDoctor - 1].queue[0]}')
        doctors[whichDoctor - 1].queue.pop(0)


# function to add a patient to a queue
def add_patient(doctors):
    # get the name of the patient to add
    nameToAdd = str(input('name to add\n'))
    while True:
        whosQueue = (input('whos queue should they be added to? (as a number)\n'))
        try:
            whosQueue = int(whosQueue)
        except:
            print('write a number')
            continue
        if whosQueue > len(doctors[whosQueue - 1].queue) and whosQueue != len(doctors[whosQueue - 1].queue):
            print('number too big')
            continue
        doctors[whosQueue - 1].queue.append(nameToAdd)
        print(f'added {nameToAdd} to the doctors queue')


# function to remove a patient from a queue
def remove_patient():
    # join all names in each queue with a comma and space for printing purposes
    s = ', '
    p = s.join(priorityQueue)
    n = s.join(normalQueue)

    # ask which patient to remove
    whom = str(input(f'who to remove\npriority: {p}\nnormal: {n}\n'))

    count = 0

    # if the patient is in the priority queue, remove them from both queues and their respective doctor lists
    if whom in priorityQueue:
        for i in priorityQueue:
            count += 1
            if i == whom:
                priorityDoctor.pop(count - 1)
                priorityQueue.pop(count - 1)

    count = 0

    # if the patient is in the normal queue, remove them from both queues and their respective doctor lists
    if whom in normalQueue:
        for i in normalQueue:
            count += 1
            if i == whom:
                normalDoctor.pop(count - 1)
                normalQueue.pop(count - 1)

    print('if the patient has been found, they have been removed from the list.')


def main(priorityQueue, normalQueue, priorityDoctor, normalDoctor):  # main function



    while True:  # loop for input protection

        callOrQueue = str(input('do you want to (c)all the next patient, (a)dd a patient, (r)emove a patient? type '
                                'clear to clear both queues.\n'))
        # calling functions based on input
        if callOrQueue == 'c':
            call_next_patient(doctors)
        elif callOrQueue == 'a':
            add_patient(doctors)
        elif callOrQueue == 'r':
            remove_patient()
        elif callOrQueue == 'clear':
            priorityQueue = []
            normalQueue = []
            priorityDoctor = []
            normalDoctor = []
            print('queues cleared')
        else:  # input protection
            print('invalid input')


if __name__ == '__main__':  # if the file name is main, run the file.

    main(priorityQueue, normalQueue, priorityDoctor, normalDoctor)
