from db import *
from datetime import datetime

# get the ID of a status by given its name
def get_status_id(status_name):
    cursor.execute('select id from task_status where status_name = %s',(status_name))
    result = cursor.fetchone()
    if result:
        # print(result['id'])
        return result['id']
    else:
        return None

# get the ID of a priority by given its name
def get_priority_id(priority_name):
    cursor.execute('select id from task_priority where priority_name = %s',(priority_name))
    result = cursor.fetchone()
    if result:
        # print(result['id'])
        return result['id']
    else:
        return None

# get the ID of a task by given its name        
def get_task_id(title):
    cursor.execute('select id from tasks where title = %s',(title))
    result = cursor.fetchone()
    if result:
        # print(result['id'])
        return result['id']
    else:
        return None

# to add new task into the database        
def add_task():
    try:    
        title = input('Enter the title : ')
        due_date = input('Enter due date in (YYYY-MM-DD) : ')
        status = input('Enter the status : ')
        sat_id = get_status_id(status)
        if not sat_id:
            print('status not found in our database')
            return None
        
        priority = input('Enter the priority : ')
        prior_id = get_priority_id(priority)
        if not prior_id:
            print('priority not found in our database')
            return None
        cursor.execute('insert into tasks(title,due_date,status_id,priority_id) values (%s , %s, %s, %s)',(title,due_date,sat_id,prior_id))
        connection.commit()
        print('Task added successfully')
    except Exception as e:
        print('Error in adding task')

# to view all tasks from the database
def retrieve_tasks():
    cursor.execute('''select t.Id,t.title,t.due_date,ts.status_name as status,tp.priority_name as priority
                        from tasks t
                        inner join task_status ts on t.status_id = ts.id
                        inner join task_priority tp on t.priority_id = tp.id
                        order by Id''')
    result = cursor.fetchall()
    print("ID | Title | Due date | Status | Priority")
    for exp in result:
        print(str(exp['Id']) + "|" + str(exp['title']) + "|" + str(exp['due_date']) + '|' + str(exp['status']) + "|" + str(exp['priority']))
    
# to update the task status (backlog,pending,in progress,done) into the database
def update_task():
    title = input("Enter the task to be updated : ")
    task_id = get_task_id(title)
    if not task_id:
        print("Task not found")
        return None
    status = input('enter the status : ')
    sat_id = get_status_id(status)
    if not sat_id:
        print('status not found in our database')
        return None
    cursor.execute('update tasks set status_id = %s where Id = %s',(sat_id,task_id))
    connection.commit()
    print('Task status updated successfully')

# to delete specific task and its entries from the database
def delete_task():
    title = input("Enter the task to be deleted : ")
    task_id = get_task_id(title)
    if not task_id:
        print("Task not found")
        return None
    cursor.execute("Delete from tasks where Id = %s",(task_id))
    connection.commit()
    print('Task deleted successfully')


# filter and view the tasks based on their status
def filter_by_status():
    status = input('enter the status : ')
    sat_id = get_status_id(status)
    if not sat_id:
        print('status not found in our database')
        return None
    cursor.execute('''select t.Id,t.title,t.due_date, ts.status_name as status
                        from tasks t
                        inner join task_status ts on t.status_id = ts.id where t.status_id = %s
                        order by Id''',(sat_id))
    result = cursor.fetchall()
    print("ID | Title | Due date | Status ")
    for exp in result:
        print(str(exp['Id']) + "|" + str(exp['title']) + "|" + str(exp['due_date']) + '|' + str(exp['status']))


# view the tasks which are both overdue(based on today's date) and status is not done
def overdue_tasks():
    today = datetime.today().date()  
    cursor.execute('''select t.Id,t.title,t.due_date, ts.status_name as status
                        from tasks t   
                        inner join task_status ts on t.status_id = ts.id where t.status_id != 4 and 
                         t.due_date < %s order by  Id ''',(today))     

    result = cursor.fetchall()  
    if result:  
        print("ID | Title | Due date | Status ")
        for exp in result:
            print(str(exp['Id']) + "|" + str(exp['title']) + "|" + str(exp['due_date']) + '|' + str(exp['status']))
    else:
        print("No overdue tasks...")        
        