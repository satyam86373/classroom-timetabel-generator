PROJECT REPORT

Classroom timetable generator

Submitted To:
Rungta International Skills University
School of Computer Science and Engineering

Course: Bachelor of Technology (B.Tech.)
Branch: Computer Science and Engineering
Semester: First Semester

Project Number: 78
Project Title: classroom timetable generator

Submitted By:
Student Name: Satyam kuamr
Erp :01714




2. INTRODUCTION

The Classroom Weekly Timetable Generator is a Python-based project designed to create a weekly class timetable automatically.

Creating a classroom timetable manually can be time-consuming and difficult because every subject must be assigned a specific number of periods throughout the week.

This project uses a Greedy Scheduling Algorithm to distribute subjects across the available days and periods.

The program selects the subject with the highest number of remaining weekly periods. If two or more subjects have the same number of remaining periods, the subject entered first is given priority.

It also follows an important scheduling constraint: a subject cannot be scheduled more than two times in a single day.

The program validates the input and generates a timetable only when the given constraints can be satisfied by its scheduling approach.

3. OBJECTIVES OF THE PROJECT

The main objectives of this project are:

To generate a weekly classroom timetable automatically.

To reduce the time required for manual timetable preparation.

To distribute subjects across different days.

To ensure that each subject appears no more than two times per day.

To select subjects based on their remaining weekly periods.

To resolve scheduling ties according to the order in which subjects are entered.

To validate user inputs and prevent invalid timetable configurations.

To demonstrate the practical application of Python programming concepts.

4. PROBLEM STATEMENT

Preparing a weekly classroom timetable manually can create scheduling difficulties.

The total number of subject periods must match the total number of available periods in a week. Additionally, no subject should be assigned more than two periods per day.

The objective is to develop a Python program that automatically generates a timetable while following these conditions:

The number of days must be between 1 and 7.

The number of periods per day must be positive.

At least one subject must be entered.

Every subject must have a positive number of weekly periods.

A subject can have a maximum of two periods per day.

Total weekly subject periods must equal total available timetable slots.

In case of a tie, the subject entered first gets priority.

5. SOFTWARE AND HARDWARE REQUIREMENTS

Software Requirements

Component

Requirement

Programming Language

Python 3

IDE

IDLE / VS Code / PyCharm

Operating System

Windows / Linux / macOS

Libraries

Python built-in modules

Interface

Command Line Interface

Hardware Requirements

Computer or laptop

Minimum 2 GB RAM

Keyboard and monitor

Basic processor capable of running Python 3

6. PYTHON CONCEPTS USED

6.1 Lists

Lists are used to store the days of the week and the generated daily timetable.

Example:

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

6.2 Dictionaries

Dictionaries store subject names and their weekly period requirements.

Example:

subjects = {"Maths": 8, "English": 6, "Science": 5}

The remaining periods of each subject are also maintained using a dictionary.

6.3 Functions

Functions divide the program into smaller and reusable parts.

The main functions are:

generate_timetable() – Generates the timetable.

display_timetable() – Displays the timetable.

get_positive_integer() – Validates numerical inputs.

main() – Controls the overall program execution.

6.4 Loops

For loops and while loops are used to:

Enter subject details.

Generate daily schedules.

Assign periods.

Validate user inputs.

6.5 Conditional Statements

If and else conditions are used to check input validity and scheduling constraints.

6.6 Exception Handling

The try and except statements handle invalid inputs and scheduling errors without unexpectedly terminating the program.

7. ALGORITHM USED

Greedy Scheduling Algorithm

This project uses a Greedy Scheduling Algorithm.

The algorithm selects the subject with the highest number of remaining periods at every scheduling step.

If multiple subjects have the same remaining periods, the subject entered earlier is selected.

Steps of the Algorithm

Start the program.

Ask the user to enter the number of days.

Ask for the number of periods per day.

Ask for the number of subjects.

Enter the subject names and their weekly periods.

Validate all entered information.

Calculate total required periods.

Calculate total available timetable slots.

Check whether both totals are equal.

Start generating the timetable day by day.

Find the eligible subjects with remaining periods.

Select the subject with the highest remaining periods.

If there is a tie, select the subject entered first.

Assign the selected subject to the timetable.

Decrease its remaining periods by one.

Repeat until all daily periods are filled.

Check whether all weekly periods have been assigned.

Display the completed timetable.

End the program.

8. WORKING OF THE PROJECT

The project works in four major stages.

Stage 1: Input Collection

The program collects:

Number of working days.

Number of periods per day.

Number of subjects.

Subject names.

Weekly periods required for each subject.

Stage 2: Input Validation

The program checks whether:

The number of days is between 1 and 7.

Periods per day are positive.

Subject names are not empty or duplicated.

Weekly periods are positive.

Each subject's weekly requirement does not exceed its maximum possible allocation.

Total subject periods equal total available slots.

Stage 3: Timetable Generation

The program uses the greedy approach to select subjects based on their remaining periods.

It also maintains a daily count for every subject to ensure that no subject is scheduled more than twice per day.

Stage 4: Timetable Display

After successful generation, the program displays the weekly timetable in a readable format.

9. IMPORTANT PROGRAM FUNCTIONS

Function

Purpose

generate_timetable()

Generates the weekly timetable using greedy scheduling.

display_timetable()

Prints the timetable in a readable format.

get_positive_integer()

Accepts and validates positive integer inputs.

main()

Manages the complete execution of the project.

Important Variables

Variable

Description

DAYS

Stores the names of the seven days.

subjects

Stores subject names and weekly periods.

remaining

Tracks the remaining periods for each subject.

daily_count

Tracks how many times a subject is scheduled in a day.

timetable

Stores the final weekly timetable.

periods_per_day

Stores the number of periods in each day.

total_required

Stores the total required weekly periods.

total_available

Stores the total available timetable slots.

10. SAMPLE INPUT

Consider the following example:

Number of days: 5

Periods per day: 6

Number of subjects: 5

Subject

Weekly Periods

Maths

8

English

7

Science

6

Computer

5

Hindi

4

Total

30

Total available slots:

5 × 6 = 30 periods

Total required periods:

8 + 7 + 6 + 5 + 4 = 30 periods

Therefore, the total required periods match the available timetable slots.

11. SAMPLE OUTPUT

CLASSROOM TIMETABLE GENERATOR
--------------------------------
Enter number of days (1-7): 5
Enter periods per day: 6
Enter number of subjects: 5

Enter name of subject 1: Maths
Enter weekly periods for Maths: 8

Enter name of subject 2: English
Enter weekly periods for English: 7

Enter name of subject 3: Science
Enter weekly periods for Science: 6

Enter name of subject 4: Computer
Enter weekly periods for Computer: 5

Enter name of subject 5: Hindi
Enter weekly periods for Hindi: 4

==========================================
             WEEKLY TIMETABLE
==========================================
Mon: Maths, English, Science, Computer, Hindi, Maths
Tue: English, Science, Computer, Hindi, Maths, English
Wed: Science, Computer, Maths, English, Hindi, Maths
Thu: Computer, English, Science, Maths, English, Computer
Fri: Maths, Science, English, Computer, Hindi, Science
==========================================

Note: This is an illustrative output format. The actual timetable is determined by the program's greedy scheduling logic.

12. VALIDATION AND ERROR HANDLING

The project includes several validation checks to ensure correct execution.

Condition

Error Message

Invalid number of days

Days must be a whole number from 1 to 7.

Invalid periods per day

Periods per day must be a positive whole number.

No subjects entered

Enter at least one subject.

Empty subject name

Subject names cannot be empty.

Invalid weekly periods

Weekly periods must be a positive whole number.

Subject exceeds daily limit

Subject cannot exceed two periods per day.

Total periods do not match

Total weekly periods must equal available slots.

Scheduling failure

A valid timetable could not be generated with the given constraints.

These validation checks make the program more reliable and user-friendly.

13. ADVANTAGES OF THE PROJECT

Automatically generates a weekly timetable.

Saves time and reduces manual effort.

Maintains the maximum two-period daily subject limit.

Uses a simple and understandable scheduling algorithm.

Provides automatic input validation.

Handles invalid inputs using exception handling.

Gives priority to subjects with more remaining periods.

Uses the original subject entry order to resolve ties.

14. LIMITATIONS OF THE PROJECT

The program uses a greedy scheduling approach, which does not guarantee a solution for every possible valid arrangement.

It does not consider teacher availability.

It does not consider classroom availability.

It does not include lunch breaks or free periods.

It does not provide a graphical user interface.

It does not save the generated timetable to an external file.

15. FUTURE SCOPE

The project can be improved in the future by adding:

A graphical user interface (GUI).

Teacher availability management.

Classroom allocation.

Lunch breaks and free periods.

Export options for PDF and Excel.

Automatic timetable saving.

More advanced scheduling algorithms.

Separate timetables for different classes.

These improvements can make the project more useful for schools and educational institutions.

16. CONCLUSION

The Classroom Weekly Timetable Generator successfully demonstrates how Python programming can be used to solve a practical scheduling problem.

The project combines important Python concepts such as lists, dictionaries, functions, loops, conditional statements, input validation, and exception handling.

By implementing a Greedy Scheduling Algorithm, the program automatically assigns subjects according to their remaining weekly periods while maintaining the maximum limit of two periods per subject per day.

This project helped develop a better understanding of problem-solving, logical thinking, data structures, and scheduling techniques in Python.

Overall, it is a simple and useful application of Python programming that can be further developed into a more advanced classroom management system.

17. REFERENCES

Python Official Documentation – https://docs.python.org/3/

Python Programming Fundamentals.

Python Lists and Dictionaries.

Python Functions and Exception Handling.

Greedy Algorithm and Scheduling Concepts.

END OF PROJECT REPORT
