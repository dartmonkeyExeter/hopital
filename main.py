# initialize empty queues and doctor lists

doctors = []

class Doctor:
    def __init__(self, name, queue):
        self.queue = queue
        self.name = name

def doctor_define(doctors):
    doctors = []
    while True:
        num_doctors = input('how many doctors are here today?\n')
        try:
            num_doctors = int(num_doctors)
        except:
            print('please insert an integer value.')
            continue
        if num_doctors <= 0:
            print("there must be at least 1 doctor, please try again")
            continue
        break

    for i in range(num_doctors):
        name = input(f"enter the name of doctor {i + 1}: ")
        queue = []
        doctors.append(Doctor(name, queue))

    for i, doctor in enumerate(doctors):
        print(f"Doctor {i + 1}: {doctor.name}")


# function to call the next patient
def call_next_patient(doctors):
    while True:
        whosQueue = (input('whos queue should be called from? (as a number)\n'))
        try:
            whosQueue = int(whosQueue)
        except:
            print('write a number')
            continue
        if whosQueue <= 0:
            print('number too small') 
            continue
        if not doctors[whosQueue - 1].queue:
            print('that doctors queue is empty')
            continue 
        if whosQueue - 1 > len(doctors):
            print('number too big')
            continue
        else:
            print(f'the next patient in doctor {doctors[whosQueue - 1].name}s queue is {doctors[whosQueue - 1].queue[0]}')
            doctors[whosQueue - 1].queue.pop(0)
            break


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
        if whosQueue <= 0:
            print('number too small') 
            continue
        if whosQueue - 1 > len(doctors):
            print('number too big')
            continue
        else:
            print(f'added {nameToAdd} to {doctors[whosQueue - 1].name}s queue')
            doctors[whosQueue - 1].queue.append(nameToAdd)
            break


def main():  # main function
    doctor_define(doctors)
    while True:  # loop for input protection
        callOrQueue = str(input('do you want to (c)all the next patient, (a)dd a patient, or (r)edfine the doctor list\n'))
        # calling functions based on input
        if callOrQueue == 'c':
            all_queues_empty = True
            for i in doctors:
                if i.queue:
                    all_queues_empty = False
                    break
            if all_queues_empty:
                print("all queues are empty")
            else:
                call_next_patient(doctors)
        elif callOrQueue == 'a':
            add_patient(doctors)
        elif callOrQueue == 'r':
            doctor_define(doctors)
        else:  # input protection
            print('invalid input')


if __name__ == '__main__':  # if the file name is main, run the file.

    main()
