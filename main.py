# initialize empty queues and doctor lists

class Doctor:
    def __init__(self, name, queue):
        self.queue = queue
        self.name = name


def doctor_define():
    doctors = []
    while True:
        num_doctors = input('how many doctors are here today?\n')
        try:
            num_doctors = int(num_doctors)
        except ValueError:
            print('please insert an integer value.')
            continue
        if num_doctors <= 0:
            print("there must be at least 1 doctor, please try again")
            continue
        break

    for i in range(num_doctors):
        name = input(f"enter the name of doctor {i + 1}: ").lower()
        queue = []
        doctors.append(Doctor(name, queue))

    for i, doctor in enumerate(doctors):
        print(f"Doctor {i + 1}: {doctor.name}")
    return doctors


def experimental_add(doctors):
    where_is_that_doctor = 0
    name_to_add = str(input('name to add\n').lower())
    while True:
        whos_queue = input("who's queue should they be added to?\n").lower()
        for doctor in doctors:
            if doctor.name.lower() == whos_queue:
                where_is_that_doctor = doctor
                break
        else:
            print("No doctor found with that name.")
            continue
        break
    print(f'added {name_to_add} to {where_is_that_doctor.name}s queue')
    where_is_that_doctor.queue.append(name_to_add)


def experimental_call(doctors):
    where_is_that_doctor = 0
    while True:
        whos_queue = input("who's queue should they be added to?\n").lower()
        for doctor in doctors:
            if doctor.name.lower() == whos_queue:
                where_is_that_doctor = doctor
                break
        else:
            print("No doctor found with that name.")
            continue
        break
    print(
        f'the next patient in doctor {where_is_that_doctor.name}s queue is '
        f'{where_is_that_doctor.queue[0]}')
    where_is_that_doctor.queue.pop(0)


# function to call the next patient
def call_next_patient(doctors):
    while True:
        whos_queue = (input("whos queue should be called from? (as a number)\n"))
        try:
            whos_queue = int(whos_queue)
        except ValueError:
            print('write a number')
            continue
        if whos_queue <= 0:
            print('number too small')
            continue
        if not doctors[whos_queue - 1].queue:
            print('that doctors queue is empty')
            continue
        if whos_queue - 1 > len(doctors):
            print('number too big')
            continue
        else:
            print(
                f'the next patient in doctor {doctors[whos_queue - 1].name}s queue is '
                f'{doctors[whos_queue - 1].queue[0]}')
            doctors[whos_queue - 1].queue.pop(0)
            break


# function to add a patient to a queue
def add_patient(doctors):
    # get the name of the patient to add
    name_to_add = str(input('name to add\n'))
    while True:
        whos_queue = (input('whos queue should they be added to? (as a number)\n'))
        try:
            whos_queue = int(whos_queue)
        except ValueError:
            print('write a number')
            continue
        if whos_queue <= 0:
            print('number too small')
            continue
        if whos_queue - 1 > len(doctors):
            print('number too big')
            continue
        else:
            print(f'added {name_to_add} to {doctors[whos_queue - 1].name}s queue')
            doctors[whos_queue - 1].queue.append(name_to_add)
            break


def main():  # main function
    doctors = doctor_define()
    while True:  # loop for input protection
        call_or_queue = str(
            input('do you want to (c)all the next patient, (a)dd a patient, '
                  'or (r)edfine the doctor list\n').strip(' ').lower())
        # calling functions based on input
        if call_or_queue == 'c':
            all_queues_empty = True
            for i in doctors:
                if i.queue:
                    all_queues_empty = False
                    break
            if all_queues_empty:
                print("all queues are empty")
            else:
                experimental_call(doctors)
        elif call_or_queue == 'a':
            experimental_add(doctors)
        elif call_or_queue == 'r':
            doctors = doctor_define()
        else:  # input protection
            print('invalid input')


if __name__ == '__main__':  # if the file name is main, run the file.
    main()
