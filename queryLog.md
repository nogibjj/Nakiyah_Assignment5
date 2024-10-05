```sql
CREATE TABLE worker_health (
    Employee_ID NUMERIC PRIMARY KEY,            
    Age INTEGER,                                
    Job_Role TEXT,                              
    Industry TEXT,                              
    Years_of_Experience INTEGER,                
    Work_Location TEXT,                         
    Hours_Worked_Per_Week INTEGER,              
    Mental_Health_Condition TEXT,               
    Access_to_Mental_Health_Resources BOOLEAN);
```

```sql
SELECT * FROM worker_health LIMIT 20
```

```sql
INSERT INTO worker_health 
                 (Employee_ID, Age, Job_Role, Industry, Years_of_Experience, Work_Location, Hours_Worked_Per_Week, 
                  Mental_Health_Condition, Access_to_Mental_Health_Resources) 
                 VALUES (EMP90005, 28, Data Analyst, Finance, 3, Onsite, 45, Anxiety, False);
```

```sql
SELECT * FROM worker_health WHERE Employee_ID = EMP90005
```

```sql
INSERT INTO worker_health 
                 (Employee_ID, Age, Job_Role, Industry, Years_of_Experience, Work_Location, Hours_Worked_Per_Week, 
                  Mental_Health_Condition, Access_to_Mental_Health_Resources) 
                 VALUES (EMP90006, 40, Data Scientist, IT, 15, Hybrid, 40, None, True);
```

```sql
SELECT * FROM worker_health WHERE Employee_ID = EMP90006
```

```sql
CREATE TABLE worker_health (
    Employee_ID NUMERIC PRIMARY KEY,            
    Age INTEGER,                                
    Job_Role TEXT,                              
    Industry TEXT,                              
    Years_of_Experience INTEGER,                
    Work_Location TEXT,                         
    Hours_Worked_Per_Week INTEGER,              
    Mental_Health_Condition TEXT,               
    Access_to_Mental_Health_Resources BOOLEAN);
```

```sql
SELECT * FROM worker_health LIMIT 20
```

```sql
INSERT INTO worker_health 
                 (Employee_ID, Age, Job_Role, Industry, Years_of_Experience, Work_Location, Hours_Worked_Per_Week, 
                  Mental_Health_Condition, Access_to_Mental_Health_Resources) 
                 VALUES (EMP90005, 28, Data Analyst, Finance, 3, Onsite, 45, Anxiety, False);
```

```sql
SELECT * FROM worker_health WHERE Employee_ID = EMP90005
```

```sql
INSERT INTO worker_health 
                 (Employee_ID, Age, Job_Role, Industry, Years_of_Experience, Work_Location, Hours_Worked_Per_Week, 
                  Mental_Health_Condition, Access_to_Mental_Health_Resources) 
                 VALUES (EMP90006, 40, Data Scientist, IT, 15, Hybrid, 40, None, True);
```

```sql
SELECT * FROM worker_health WHERE Employee_ID = EMP90006
```

```sql
UPDATE worker_health SET 
                 Age = 28, Job_Role = Software Engineer, Industry = Tech, Years_of_Experience = 3, 
                 Work_Location = Onsite, Hours_Worked_Per_Week = 45, Mental_Health_Condition = Anxiety, 
                 Access_to_Mental_Health_Resources = False 
                 WHERE Employee_ID = EMP90005;
```

```sql
SELECT * FROM worker_health WHERE Employee_ID = EMP90005
```

```sql
DELETE FROM worker_health WHERE Employee_ID = 'EMP90006';
```

```sql
SELECT * FROM worker_health WHERE Employee_ID = EMP90006
```

