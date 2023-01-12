import datetime
import uuid

class task_manager:
    def __init__(self) -> None:
        self.task_list = []


    def add_new_task(self):
        self.task_name = input('Enter New Task: ')
        self.created_time = datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S')
        self.update_time = 'NA'
        self.complete_time = 'NA'
        self.task_done = False
        self.id = uuid.uuid4()
        self.make_tup = Add_new_Task(self.id, self.task_name, self.created_time, self.update_time, self.task_done, self.complete_time)
        self.task_list.append(self.make_tup)


    def show_all_task(self):
        for tups in self.task_list:
            print(f'ID: {tups.id}\nTask: {tups.task_name}\nCreated Time: {tups.created_time}\nUpdate Time: {tups.update_time}\nComplete: {tups.task_done}\nCompleted Time: {tups.complete_time}')
            print()


    def show_incom_task(self):
        self.flag = 0
        for tups in self.task_list:
            if tups.task_done == False:
                self.flag = 1
                print(f'ID: {tups.id}\nTask: {tups.task_name}\nCreated Time: {tups.created_time}\nUpdate Time: {tups.update_time}\nComplete: {tups.task_done}\nCompleted Time: {tups.complete_time}')
                print()
        if self.flag == 0:
            print('No Incomplete Task is Available')
        print()


    def show_completed_task(self):
        self.flag = 0
        for tups in self.task_list:
            if tups.task_done == True:
                self.flag = 1
                print(f'ID: {tups.id}\nTask: {tups.task_name}\nCreated Time: {tups.created_time}\nUpdate Time: {tups.update_time}\nComplete: {tups.task_done}\nCompleted Time: {tups.complete_time}')
                print()
        if self.flag == 0:
            print('No Completed Task is Available')
        print()


    def update_task(self):
        print('Select Which Task To Update\n')
        self.flag = 0
        for tups in self.task_list:
            if tups.task_done == False:
                self.flag = 1
                print(f'Task No - {self.task_list.index(tups) + 1}')
                print(f'ID: {tups.id}\nTask: {tups.task_name}\nCreated Time: {tups.created_time}\nUpdate Time: {tups.update_time}\nComplete: {tups.task_done}\nCompleted Time: {tups.complete_time}')
                print()

        if self.flag == 0:
            print('No Task To Update')
        else:
            self.task_no = int(input('Enter Task No: '))
            self.new_task_name = input('Enter New Task: ')
            self.new_update_time = datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S')
            for t_tups in self.task_list:
                if (self.task_list.index(t_tups) + 1) == self.task_no:
                    t_tups.task_name = self.new_task_name
                    t_tups.update_time = self.new_update_time
            print('Task Updated Successfully\n')
        print()


    def mark_task_as_complete(self):
        print('Select Which Task To Complete\n')
        self.flag = 0
        for tups in self.task_list:
            if tups.task_done == False:
                self.flag = 1
                print(f'Task No - {self.task_list.index(tups) + 1}')
                print(f'ID: {tups.id}\nTask: {tups.task_name}\nCreated Time: {tups.created_time}\nUpdate Time: {tups.update_time}\nComplete: {tups.task_done}\nCompleted Time: {tups.complete_time}')
                print()

        if self.flag == 0:
            print('\nNo Task To Complete')
        else:
            self.task_no = int(input('Enter Task No: '))
            self.new_complete_time = datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S')
            for tups in self.task_list:
                if self.task_list.index(tups) + 1 == self.task_no:
                    tups.task_done = True
                    tups.complete_time = self.new_complete_time
            print('Task Completed Successfully\n')
        print()



class Add_new_Task:
    def __init__(self, id, task_name, created_time, update_time, task_done, complete_time):
        self.id = id
        self.task_name = task_name
        self.created_time = created_time
        self.update_time = update_time
        self.task_done = task_done
        self.complete_time = complete_time



Task_obj = task_manager()

while(True):
    print("1. Add New Task\n2. Show All Task\n3. Show Incomplete Tasks\n4. Show Completed Tasks\n5. Update Task\n6. "
          "Mark A Task Completed")
    print()
    choice = int(input('ENTER OPTION: '))
    if choice == 1:
        Task_obj.add_new_task()
        print('Task Created Successfully\n')
    elif choice == 2:
        Task_obj.show_all_task()
    elif choice == 3:
        Task_obj.show_incom_task()
    elif choice == 4:
        Task_obj.show_completed_task()
    elif choice == 5:
        Task_obj.update_task()
    elif choice == 6:
        Task_obj.mark_task_as_complete()
    else:
        break
