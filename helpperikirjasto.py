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
    fileName = input("Give csv-file where volunteers are listed.")
    volunteers = readFile(fileName)
    return volunteers

def readFile(fileName):
    rows = 0
    volunteers = []
    try:
        file = open(fileName, 'r')
        file.readline() # Reading the headers away.

        while True:
            row = file.readline()
            if len(row) == 0:
                break
            else:
                data = row.split(';')
                volunteer = VOLUNTEER()
                volunteer.name = data[0]
                volunteer.arrive_time = data[1]
                volunteer.leaving_time = data[2]
                volunteer.can_do_tasks = get_tasks(data)
                volunteers.append(volunteer)
                rows += 1

    except Exception:
        print("Error handling file {0}, try again.".format(fileName))
    return volunteers


def get_tasks(data):
    # Tiskit, imurointi, WC, rannekkeet, kahvila, jne.
    can_do_tasks = []
    for i in data[3:]:
        if data[i] == "1":
            can_do_tasks[i-2] = 1
        else:
            can_do_tasks[i-2] = 0
    return can_do_tasks