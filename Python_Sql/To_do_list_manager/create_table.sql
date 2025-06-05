create database To_Do_List_Manager;
use to_do_list_manager;

create table task_status (Id int Primary key,status_name varchar(50) unique);
alter table task_status modify column Id int auto_increment;

create table task_priority(Id int Primary key,priority_name varchar(50) unique);
alter table task_priority modify column Id int auto_increment;

create table tasks(Id int Primary key auto_increment,title varchar(50) unique,due_date date,status_id int,
 priority_id int,foreign key (status_id) references task_status(Id)  on delete cascade
 on update cascade,
 foreign key (priority_id) references task_priority(Id)
 on delete cascade
 on update cascade);
 
 insert into task_status (status_name) values 
('Backlog'),('Pending'),('In progress'),('Done');
 select * from task_status order by Id;
 
 insert into task_priority (priority_name) values 
('Urgent'),('High'),('Medium'),('Low');
select * from task_priority order by Id;

insert into tasks(title,due_date,status_id,priority_id) values ('complete assessment','2025-04-23',1,2),
 ('submit monthly report','2025-04-21',3,1),('backup files','2025-04-20',2,1);
 
select * from tasks order by Id;
select *from tasks;

select t.Id,t.title,t.due_date,ts.status_name as status,tp.priority_name as priority
                        from tasks t
                        inner join task_status ts on t.status_id = ts.id
                        inner join task_priority tp on t.priority_id = tp.id
                        order by Id;
 
 
-- select title,due_date from tasks where due_date < '2025-04-23' AND 
                --    status_id != (select id from task_status where status_name = 'Done');
                   
                   
select t.Id,t.title,t.due_date, ts.status_name as status
                        from tasks t   
					    inner join task_status ts on t.status_id = ts.id where t.status_id != 4 and  due_date < '2025-04-23'
                        order by  Id                  
                   


 

