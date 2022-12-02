# Grader API

Grader is an online gradebook app which teachers can use to store student grades and generate real time data to track class progress. The app also supports a view for students to see current grades as well as feedback on individual assignments. 

This API supports the client side of the Grader app. The server is built with django and uses a postgresql database to store users' class, grade and assignment information. The API will use SQL's relational features to generate several different "gradebook" views. Teacher users on the client-side will then have different options of how to see and manipulate grades. Using joins will streamline spreadsheet generation where teachers can choose to either see details for assignments (i.e. assignments as rows) or students (students as rows).

# User stories

## As a client user I want to...
- Have full CRUD functionality on assignments, courses, and grades
- be able to call to routes which handle joins to effectively create different tables based on the view I want 

# Technology used

- django framework
- postgresql db
- pandas to help generate distribution views (later versions matbe)

# Entity Relationships

[ERD generated with drawsql](https://drawsql.app/teams/mb-11/diagrams/grader)

## Joining Entities
At bottom, information necessary for a gradebook which would have both a teacher and a student view is embedded in relations which can be many-to-many, one-to-many, or many-to-one. The ERD above is highly compartmentalized by design to allow for dynamic joins to allow more user customization. Beyond users, teachers, and students, the core entities which are, in my mind, crucial for the gradebook are the section and the grade itself. The section table here will function as a through table which will allow teachers to have many students across different courses and different sections of the same course. In turn, students will be associated with all their teachers by reference of each of their appearances in the section table. The grade table has it's own independent function as the container for qualitative and quantitative information about student performance (as well the assigning teacher). It is also effectively a through table for students, and assignments. Each assignment will be given to many students and each student will have many assignments. 

# Routing Table
## /accounts
--> / GET 
    --> Index  user accounts
--> /signup POST
    --> create a user account
--> /teachers GET POST
    --> index, create a teacher (association with user is handled automatically by serializer)
--> /teachers/:pk GET PATCH DELETE
    --> retrieve, update, destroy a teacher (automatically destorys the user)
--> /students GET POST
    --> index, create students. Student instances do not have to be associated with user
--> /students GET PATCH DELETE
    --> retrieve, update, destroy a student

## /courses
--> /, GET POST
    --> Index, create a course and related sections
--> /:pk GET PATCH DELETE
    --> retrieve, update, destroy a course
--> /:course_id/sections/ GET POST
    --> Index, create sections 
--> /:course_id/sections/:pk GET PATCH DELETE
    --> retrieve, update, destroy a section
--> /myclasses/ GET
    --> for students only to index the sections to which they belong
--> /students/:section_id/ PATCH   
    --> to be used by a teacher to add a student to their course
--> /students/join/:student_id> PATCH
    --> for a student to use a join code to join a section

## /gradebook
--> /assignments/:course_id GET POST
    --> index (by teacher), create an assignment 
--> /assignments/update/:pk/ GET PATCH DELETE
    --> retrieve, update, destroy an assignment 
--> /assignments/student/ GET
    --> index assignments (student)
--> /assignments/:assignment_id/grades/ GET POST 
    --> index, create grades for an assignment
--> /grades/:pk/ GET PATCH DELETE
    --> retrieve, update, destroy a grade
--> /mygrades/ GET
    --> index grades (student)
--> /courses/:course_id>/ GET
    --> index all grades for a course (meant for teacher use)
--> /grades/updatemany/ PATCH
    --> batch update for many grade (values only)