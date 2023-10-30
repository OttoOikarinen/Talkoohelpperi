class VOLUNTEER():
    name = ""
    phone_number = ""
    arrive_time = ""
    leaving_time = ""
    can_do_tasks = []
    tasks_sum = 0
    task_length_combined = 0

class VOLUNTEER_JOB():
    task = ""
    task_length = 0
    task_weight = 0


class VOLUNTEER_JOB_INSTANCE():
    type = None
    start_time = ""
    end_time = ""
    volunteer = ""

class EVENT():
    name = ""
    location = ""
    amount_of_volunteers = 0


def generate_volunteer_list():
    print("we are here")
    fileName = input("Give csv-file where volunteers are listed: ")
    volunteers = readFile(fileName)
    return volunteers

def readFile(fileName):
    rows = 0
    volunteers = []
    
    file = open(fileName, 'r')
    file.readline() # Reading the headers away.

    while True:
        row = file.readline()
        if len(row) == 0:
            break
        else:
            data = row.split(';')
            data = data[:-1]
            volunteer = VOLUNTEER()
            volunteer.name = data[0]
            volunteer.phone_number = data[1]
            volunteer.arrive_time = data[2]
            volunteer.leaving_time = data[3]
            volunteer.can_do_tasks = get_tasks(data)
            volunteers.append(volunteer)
            rows += 1

    
    return volunteers


def get_tasks(data):
    # Tiskit, imurointi, WC, rannekkeet, kahvila, jne.
    can_do_tasks = []
    for item in data[3:]:
        if item == "1":
            can_do_tasks.append(1)
        else:
            can_do_tasks.append(0)
    return can_do_tasks

def print_all_volunteers(volunteers):
    print("### Printing all volunteers ###")
    for i in volunteers:
        print_volunteer(i)
        print()
    return 0

def print_volunteer(volunteer):

    print(volunteer.name)
    print(volunteer.phone_number)
    print(volunteer.arrive_time)
    print(volunteer.leaving_time)
    print(volunteer.can_do_tasks)
    print(volunteer.tasks_sum)
    print(volunteer.task_length_combined)

    return 0
