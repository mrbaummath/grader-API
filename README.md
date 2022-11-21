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
- pandas to help generate distribution views

# Entity Relationships

[ERD generated with drawsql](https://drawsql.app/teams/mb-11/diagrams/grader)

## Joining Entities
At bottom, information necessary for a gradebook which would have both a teacher and a student view is embedded in relations which can be many-to-many, one-to-many, or many-to-one. The ERD above is highly compartmentalized by design to allow for dynamic joins to allow more user customization. Beyond users, teachers, and students, the core entities which are, in my mind, crucial for the gradebook are the section and the grade itself. The section table here will function as a through table which will allow teachers to have many students across different courses and different sections of the same course. In turn, students will be associated with all their teachers by reference of each of their appearances in the section table. The grade table has it's own independent function as the container for qualitative and quantitative information about student performance (as well the assigning teacher). It is also effectively a through table for students, and assignments. Each assignment will be given to many students and each student will have many assignments. 

# Routing Table

| URL                                                          | HTTP Verb | Action                                                |
|--------------------------------------------------------------|-----------|-------------------------------------------------------|
| /user                                                        | POST      | create user                                           |
| /user/:id                                                    | GET       | get user details                                      |
| /user/:id                                                    | PATCH     | update user details                                   |
| /user/:id                                                    | DELETE    | destroy user                                          |
| /teachers                                                    | POST      | create teacher account                                |
| /teachers/:teacher_id                                        | GET       | get teacher details                                   |
| /teacher/:teacher_id                                         | PATCH     | update teacher details                                |
| /teachers/:teacher_id/classes                                | GET       | index all classes of a teacher                        |
| /teachers/:teacher_id/classes                                | POST      | create class and sections                             |
| /teachers/:teacher_id/classes/:class_id                      | GET       | get class/section details                             |
| /teachers/:teacher_id/classes/:class_id                      | PATCH     | update class/section details                          |
| /teachers/:teacher_id/classes/:class_id                      | DELETE    | delete class/section                                  |
| /teachers/:teacher_id/classes/:class_id/students             | GET       | get students details from a particular class          |
| /teachers/:teacher_id/classes/:class_id/students             | POST      | create student from teacher view                      |
| /teachers/:teacher_id/classes/:class_id/students/:student_id | DELETE    | remove student from teacher view                      |
| /teachers/:teacher_id/classes/:class_id/students/:student_id | PATCH     | update student from teacher view                      |
| /teachers/:teacher_id/classes/assignments                    | GET       | index all assignments from a class                    |
| /teachers/:teacher_id/classes/assignments                    | POST      | create assignment for a class                         |
| /teachers/:teacher_id/classes/assignments/:assignment_id     | GET       | get assignment details                                |
| /teachers/:teacher_id/classes/assignments/:assignment_id     | POST      | create grade                                          |
| /teachers/:teacher_id/classes/assignments/:assignment_id     | PATCH     | update assignment or grade                            |
| /teachers/:teacher_id/classes/assignments/:assignment_id     | DELETE    | delete assignment/grade                               |
| /teachers/:teacher_id/gradebooks                             | GET       | index all gradebooks aross courses                    |
| /teachers/:teacher_id/gradebooks/:class_id?view=<view>       | GET       | see gradebooks for a class, configured w/ view option |
| /teachers/:teacher_id/gradebooks/:class_id                   | PATCH     | update gradebook                                      |
| /teachers/:teacher_id/gradebooks/:class_id                   | PATCH     | destroy gradebook                                     |
| /students?teacher_code=<teacher_code>                        | POST      | create student account (student view)                 |
| /students/:student_id                                        | GET       | get detailed view for student (student view)          |
| /students/:student_id                                        | PATCH     | update student details (student view)                 |
| /students/:student_id                                        | DELETE    | delete student as user                                |