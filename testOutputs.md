### Top 20 Record

**Command:** `python3 main.py query`

**Return code:** 0

**STDOUT:**
```plaintext
Querying data...
Top 20 rows of the worker_health table:
+-------------+-----+-------------------+---------------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
| Employee_ID | Age |     Job_Role      |   Industry    | Years_of_Experience | Work_Location | Hours_Worked_Per_Week | Mental_Health_Condition | Access_to_Mental_Health_Resources |
+-------------+-----+-------------------+---------------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
|   EMP0001   | 32  |        HR         |  Healthcare   |         13          |    Hybrid     |          47           |       Depression        |                 0                 |
|   EMP0002   | 40  |  Data Scientist   |      IT       |          3          |    Remote     |          52           |         Anxiety         |                 0                 |
|   EMP0003   | 59  | Software Engineer |   Education   |         22          |    Hybrid     |          46           |         Anxiety         |                 0                 |
|   EMP0004   | 27  | Software Engineer |    Finance    |         20          |    Onsite     |          32           |       Depression        |                 1                 |
|   EMP0005   | 49  |       Sales       |  Consulting   |         32          |    Onsite     |          35           |          None           |                 1                 |
|   EMP0006   | 59  |       Sales       |      IT       |         31          |    Hybrid     |          39           |          None           |                 0                 |
|   EMP0007   | 31  |       Sales       |      IT       |         24          |    Remote     |          51           |         Anxiety         |                 1                 |
|   EMP0008   | 42  |  Data Scientist   | Manufacturing |          6          |    Onsite     |          54           |       Depression        |                 0                 |
|   EMP0009   | 56  |  Data Scientist   |  Healthcare   |          9          |    Hybrid     |          24           |          None           |                 1                 |
|   EMP0010   | 30  |        HR         |      IT       |         28          |    Hybrid     |          57           |       Depression        |                 1                 |
|   EMP0011   | 33  | Software Engineer |    Finance    |         17          |    Remote     |          48           |          None           |                 1                 |
|   EMP0012   | 47  |     Marketing     |  Consulting   |         31          |    Hybrid     |          26           |          None           |                 1                 |
|   EMP0013   | 40  |     Marketing     |  Consulting   |          1          |    Remote     |          21           |       Depression        |                 1                 |
|   EMP0014   | 51  |     Designer      | Manufacturing |          5          |    Hybrid     |          45           |         Anxiety         |                 0                 |
|   EMP0015   | 36  |  Project Manager  |    Retail     |         23          |    Remote     |          59           |         Anxiety         |                 1                 |
|   EMP0016   | 56  |       Sales       |  Healthcare   |         13          |    Remote     |          44           |         Anxiety         |                 0                 |
|   EMP0017   | 33  |        HR         |   Education   |          3          |    Onsite     |          52           |          None           |                 0                 |
|   EMP0018   | 45  |  Data Scientist   |  Consulting   |         20          |    Onsite     |          37           |         Burnout         |                 1                 |
|   EMP0019   | 49  | Software Engineer |      IT       |         30          |    Remote     |          36           |         Anxiety         |                 0                 |
|   EMP0020   | 59  | Software Engineer |  Consulting   |         13          |    Remote     |          59           |         Anxiety         |                 0                 |
+-------------+-----+-------------------+---------------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+

```

**STDERR:**
```plaintext
0.00s - Debugger warning: It seems that frozen modules are being used, which may
0.00s - make the debugger miss breakpoints. Please pass -Xfrozen_modules=off
0.00s - to python to disable frozen modules.
0.00s - Note: Debugging will proceed. Set PYDEVD_DISABLE_FILE_VALIDATION=1 to disable this validation.

```

### Add Record 1

**Command:** `python3 main.py create EMP90005 28 Data Analyst Finance 3 Onsite 45 Anxiety False`

**Return code:** 0

**STDOUT:**
```plaintext
Create Record
Record with Employee_ID EMP90005 created successfully.
Record with Employee_ID EMP90005:
+-------------+-----+--------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
| Employee_ID | Age |   Job_Role   | Industry | Years_of_Experience | Work_Location | Hours_Worked_Per_Week | Mental_Health_Condition | Access_to_Mental_Health_Resources |
+-------------+-----+--------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
|  EMP90005   | 28  | Data Analyst | Finance  |          3          |    Onsite     |          45           |         Anxiety         |               False               |
+-------------+-----+--------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+

```

**STDERR:**
```plaintext
0.00s - Debugger warning: It seems that frozen modules are being used, which may
0.00s - make the debugger miss breakpoints. Please pass -Xfrozen_modules=off
0.00s - to python to disable frozen modules.
0.00s - Note: Debugging will proceed. Set PYDEVD_DISABLE_FILE_VALIDATION=1 to disable this validation.

```

### Add Record 2

**Command:** `python3 main.py create EMP90006 40 Data Scientist IT 15 Hybrid 40 None True`

**Return code:** 0

**STDOUT:**
```plaintext
Create Record
Record with Employee_ID EMP90006 created successfully.
Record with Employee_ID EMP90006:
+-------------+-----+----------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
| Employee_ID | Age |    Job_Role    | Industry | Years_of_Experience | Work_Location | Hours_Worked_Per_Week | Mental_Health_Condition | Access_to_Mental_Health_Resources |
+-------------+-----+----------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
|  EMP90006   | 40  | Data Scientist |    IT    |         15          |    Hybrid     |          40           |          None           |               True                |
+-------------+-----+----------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+

```

**STDERR:**
```plaintext
0.00s - Debugger warning: It seems that frozen modules are being used, which may
0.00s - make the debugger miss breakpoints. Please pass -Xfrozen_modules=off
0.00s - to python to disable frozen modules.
0.00s - Note: Debugging will proceed. Set PYDEVD_DISABLE_FILE_VALIDATION=1 to disable this validation.

```

### Top 20 Record

**Command:** `python3 main.py query`

**Return code:** 0

**STDOUT:**
```plaintext
Querying data...
Top 20 rows of the worker_health table:
+-------------+-----+-------------------+---------------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
| Employee_ID | Age |     Job_Role      |   Industry    | Years_of_Experience | Work_Location | Hours_Worked_Per_Week | Mental_Health_Condition | Access_to_Mental_Health_Resources |
+-------------+-----+-------------------+---------------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
|   EMP0001   | 32  |        HR         |  Healthcare   |         13          |    Hybrid     |          47           |       Depression        |                 0                 |
|   EMP0002   | 40  |  Data Scientist   |      IT       |          3          |    Remote     |          52           |         Anxiety         |                 0                 |
|   EMP0003   | 59  | Software Engineer |   Education   |         22          |    Hybrid     |          46           |         Anxiety         |                 0                 |
|   EMP0004   | 27  | Software Engineer |    Finance    |         20          |    Onsite     |          32           |       Depression        |                 1                 |
|   EMP0005   | 49  |       Sales       |  Consulting   |         32          |    Onsite     |          35           |          None           |                 1                 |
|   EMP0006   | 59  |       Sales       |      IT       |         31          |    Hybrid     |          39           |          None           |                 0                 |
|   EMP0007   | 31  |       Sales       |      IT       |         24          |    Remote     |          51           |         Anxiety         |                 1                 |
|   EMP0008   | 42  |  Data Scientist   | Manufacturing |          6          |    Onsite     |          54           |       Depression        |                 0                 |
|   EMP0009   | 56  |  Data Scientist   |  Healthcare   |          9          |    Hybrid     |          24           |          None           |                 1                 |
|   EMP0010   | 30  |        HR         |      IT       |         28          |    Hybrid     |          57           |       Depression        |                 1                 |
|   EMP0011   | 33  | Software Engineer |    Finance    |         17          |    Remote     |          48           |          None           |                 1                 |
|   EMP0012   | 47  |     Marketing     |  Consulting   |         31          |    Hybrid     |          26           |          None           |                 1                 |
|   EMP0013   | 40  |     Marketing     |  Consulting   |          1          |    Remote     |          21           |       Depression        |                 1                 |
|   EMP0014   | 51  |     Designer      | Manufacturing |          5          |    Hybrid     |          45           |         Anxiety         |                 0                 |
|   EMP0015   | 36  |  Project Manager  |    Retail     |         23          |    Remote     |          59           |         Anxiety         |                 1                 |
|   EMP0016   | 56  |       Sales       |  Healthcare   |         13          |    Remote     |          44           |         Anxiety         |                 0                 |
|   EMP0017   | 33  |        HR         |   Education   |          3          |    Onsite     |          52           |          None           |                 0                 |
|   EMP0018   | 45  |  Data Scientist   |  Consulting   |         20          |    Onsite     |          37           |         Burnout         |                 1                 |
|   EMP0019   | 49  | Software Engineer |      IT       |         30          |    Remote     |          36           |         Anxiety         |                 0                 |
|   EMP0020   | 59  | Software Engineer |  Consulting   |         13          |    Remote     |          59           |         Anxiety         |                 0                 |
+-------------+-----+-------------------+---------------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+

```

**STDERR:**
```plaintext
(No error output)
```

### Add Record 1

**Command:** `python3 main.py create EMP90005 28 Data Analyst Finance 3 Onsite 45 Anxiety False`

**Return code:** 0

**STDOUT:**
```plaintext
Create Record
Record with Employee_ID EMP90005 created successfully.
Record with Employee_ID EMP90005:
+-------------+-----+--------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
| Employee_ID | Age |   Job_Role   | Industry | Years_of_Experience | Work_Location | Hours_Worked_Per_Week | Mental_Health_Condition | Access_to_Mental_Health_Resources |
+-------------+-----+--------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
|  EMP90005   | 28  | Data Analyst | Finance  |          3          |    Onsite     |          45           |         Anxiety         |               False               |
+-------------+-----+--------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+

```

**STDERR:**
```plaintext
(No error output)
```

### Add Record 2

**Command:** `python3 main.py create EMP90006 40 Data Scientist IT 15 Hybrid 40 None True`

**Return code:** 0

**STDOUT:**
```plaintext
Create Record
Record with Employee_ID EMP90006 created successfully.
Record with Employee_ID EMP90006:
+-------------+-----+----------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
| Employee_ID | Age |    Job_Role    | Industry | Years_of_Experience | Work_Location | Hours_Worked_Per_Week | Mental_Health_Condition | Access_to_Mental_Health_Resources |
+-------------+-----+----------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
|  EMP90006   | 40  | Data Scientist |    IT    |         15          |    Hybrid     |          40           |          None           |               True                |
+-------------+-----+----------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+

```

**STDERR:**
```plaintext
(No error output)
```

### Update Record

**Command:** `python3 main.py update EMP90005 28 Software Engineer Tech 3 Onsite 45 Anxiety False`

**Return code:** 0

**STDOUT:**
```plaintext
Updating selected record...
Record with Employee_ID EMP90005 updated successfully.
Record with Employee_ID EMP90005:
+-------------+-----+-------------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
| Employee_ID | Age |     Job_Role      | Industry | Years_of_Experience | Work_Location | Hours_Worked_Per_Week | Mental_Health_Condition | Access_to_Mental_Health_Resources |
+-------------+-----+-------------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+
|  EMP90005   | 28  | Software Engineer |   Tech   |          3          |    Onsite     |          45           |         Anxiety         |               False               |
+-------------+-----+-------------------+----------+---------------------+---------------+-----------------------+-------------------------+-----------------------------------+

```

**STDERR:**
```plaintext
(No error output)
```

### Delete Record

**Command:** `python3 main.py delete EMP90006`

**Return code:** 0

**STDOUT:**
```plaintext
Deleting selected query...
No record found for Employee_ID EMP90006

```

**STDERR:**
```plaintext
(No error output)
```

