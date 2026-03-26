[README.md](https://github.com/user-attachments/files/26280792/README.md)
# **QUIZ AND PRACTICE TEST GENERATOR**



This project is a subject-wise quiz generator designed to help students practice questions based on specific subjects and difficulty levels. It was developed as part of the Python Essentials BYOP capstone project, with the goal of making learning more interactive, personalized, and engaging.





## **TABLE OF CONTENT:**



1. ##### Problem statement
2. ##### Features
3. ##### Python concepts used
4. ##### Installation
5. ##### How to run
6. ##### How to use
7. ##### SAMPLE OUTPUT
8. ##### Challenges faced and solutions
9. ##### Future enhancements
10. ##### Learning outcomes





\------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### **1.PROBLEM STATEMENT-**



**Studying for exams is stressful enough without having to hunt down practice questions, sort them by topic, and somehow keep track of how you're actually doing. Most students either over-prepare one subject or fly blind on their weak spots.**

**This project fixes that — a subject-wise quiz generator built to make practice feel less like a chore.**





#### **2.FEATURES-**



**Core Features**

**- Subject-wise Organization - Create and manage multiple subjects**

**- Difficulty Levels - Easy, Medium, and Hard questions**

**- Random Question Selection - Unique questions each quiz**

**- Score Calculation - Automatic scoring with percentage**

**- Grade System - Letter grades based on performance**

**- Progress Tracking - Track all quiz attempts**

**- Subject Statistics - View accuracy per subject**

**- Persistent Storage - Automatic save to JSON file**



&#x20;**Additional Features**

**- View question bank with success rates**

**- Add new subjects**

**- Add custom questions**

**- Track performance over time**

**- Filter by difficulty**





#### **3.Python Concepts Used-**



**This project uses core Python concepts like:**



**-Variables and data types**

**-Lists and dictionaries**

**-Loops (for, while)**

**-Conditions (if-else)**

**-Functions**

**-Object-Oriented Programming (Classes)**

**-File handling (JSON)**

**-Exception handling (try-except)**

**-Random module**



#### **4. Installation-**



**Follow these simple steps to set up the project on your system.**



* &#x20;**Prerequisites**

**Before you begin, make sure you have:**

**Python 3.7 or higher installed**

**Git installed (optional, for cloning the repository)**



* **Clone the Repository**

**Open your terminal or command prompt and run:**

**git clone https://github.com/YOUR\_USERNAME/Quiz-Generator-BYOP.git**



* **Navigate to the Project Folder:**

**cd Quiz-Generator-BYOP**



#### **5.How To Run-**

**Run the Python file:**

**quiz\_generator.py**



#### **6.How To Use-**

* **Start the program**
* **Choose a subject**
* **Select difficulty level**
* **Answer the questions**
* **Get your score and feedback**



##### **-First Time Setup**

###### **1.Enter your name when prompted**



**The program automatically creates default subjects and questions**



**Default subjects: Python Basics, Data Structures, OOP, Databases**



###### **2.Main Menu Options:**

**==================================================**

**MAIN MENU**

**==================================================**

**1. Take Quiz**

**2. View Question Bank**

**3. Add New Subject**

**4. Add Question to Subject**

**5. Track Progress**

**6. View Subject Statistics**

**7. Exit**

**==================================================**



**--Option 1: Take Quiz**

* **Select a subject from the list**



* **Choose number of questions (1-10)**



* **Select difficulty (Easy/Medium/Hard/Mixed)**



* **Answer questions by typing A, B, C, or D**



* **Get immediate feedback and final score**





**--Option 2: View Question Bank**



* **See all questions organized by subject**



* **View difficulty level, options, and correct answers**



* **See success rates for each question**
* 



**--Option 3: Add New Subject**

* **Create a new subject category**



**Example: "Web Development", "Machine Learning"**





**--Option 4: Add Question to Subject**

* **Select subject**



* **Enter question text**



* **Add 4 options (A, B, C, D)**



* **Specify correct answer**



* **Select difficulty level**





**--Option 5: Track Progress**

* **View total quizzes taken**



* **See subject-wise performance**



* **Check latest quiz results**





**--Option 6: View Subject Statistics**

* **Total questions per subject**



* **Total attempts**



* **Overall accuracy percentage**







#### **7.Sample Output-**

**------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**



**🎓 SUBJECT-WISE QUIZ GENERATOR**

**==================================================**



**Enter your name: Kashish**



**📚 Creating new question bank...**



**👋 Welcome, Kashish!**

**📚 Available Subjects: Python Basics, Data Structures, OOP, Databases**



**==================================================**

**MAIN MENU**

**==================================================**

**1. Take Quiz**

**2. View Question Bank**

**3. Add New Subject**

**4. Add Question to Subject**

**5. Track Progress**

**6. View Subject Statistics**

**7. Exit**

**==================================================**



**Select option (1-7): 1**



**📚 SELECT SUBJECT**

**------------------------------**

**1. Python Basics**

**2. Data Structures**

**3. OOP**

**4. Databases**



**Select subject number: 2**



**📝 QUIZ SETUP**

**------------------------------**

**Available questions: 3**

**Number of questions (1-3): 2**



**🎯 DIFFICULTY LEVEL**

**1. Easy**

**2. Medium**

**3. Hard**

**4. Mixed**

**Select (1-4): 1**



**==================================================**

**QUIZ: DATA STRUCTURES**

**Questions: 2**

**Difficulty: Easy**

**==================================================**





**Question 1/2**

**\[Difficulty: EASY]**



**Which data structure uses FIFO?**



**Options:**

&#x20; **A. Stack**

&#x20; **B. Tree**

&#x20; **C. Queue**

&#x20; **D. Graph**



**Your answer (A/B/C/D): c**

**✅ Correct!**

**Score: 1/1**



**Question 2/2**

**\[Difficulty: EASY]**



**Which data structure uses LIFO?**



**Options:**

&#x20; **A. Queue**

&#x20; **B. Stack**

&#x20; **C. Array**

&#x20; **D. Linked List**



**Your answer (A/B/C/D): b**

**✅ Correct!**

**Score: 2/2**



**==================================================**

**QUIZ RESULTS**

**==================================================**

**Subject: Data Structures**

**Final Score: 2/2**

**Percentage: 100.0%**

**Grade: A+ (Excellent!)**

**==================================================**



**✅ Progress saved!**



**==================================================**

**MAIN MENU**

**==================================================**

**1. Take Quiz**

**2. View Question Bank**

**3. Add New Subject**

**4. Add Question to Subject**

**5. Track Progress**

**6. View Subject Statistics**

**7. Exit**

**==================================================**



**Select option (1-7): 7**



**👋 Goodbye, Kashish!**

**📊 You've completed 1 quizzes**

**Keep practicing! 🎓**

**------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**



#### **8.Challenges Faced \& Solutions-**

###### 

###### **Challenge 1: Data Persistence**

**Problem: Questions and progress were lost when program closed**

**Solution: Implemented JSON file storage with save/load functions**



###### **Challenge 2: Converting Old Data Format**

**Problem: Old version used list format, new version uses dictionary**

**Solution: Added conversion logic in load\_data() to handle both formats**



###### **Challenge 3: Input Validation**

**Problem: Users entering invalid inputs caused crashes**

**Solution: Added while loops with try-except blocks for all inputs**

###### 

###### **Challenge 4: Random Question Selection**

**Problem: Same questions appearing in same quiz**

**Solution: Used random.sample() which selects unique questions**

###### 

###### **Challenge 5: Subject Organization**

**Problem: Questions scattered without organization**

**Solution: Created Subject class and dictionary-based storage system**



#### **9.Future Enhancements:**



**- Add timer for timed quizzes**

**-Generate performance charts and graphs**

**-Create GUI version using Tkinter**

**-Make web version with Flask**

**-Mobile app version**

**-Multi-user support with login**

**-Identify weak areas automatically**

**-Email quiz results**

**-Leaderboard system**



#### **10.Learning Outcomes:**



**Through this project, I learned:**



* **Object-Oriented Programming - Creating and using classes effectively**
* **File I/O - Reading/writing JSON files**
* **Data Structures - Using dictionaries and lists effectively**
* **Error Handling - Making robust programs**
* **Modular Design - Breaking code into manageable functions**
* **User Experience - Creating intuitive menus and prompts**
* **Version Control - Using Git for project management**



**Author**

**Name: Kashish A**

**Student ID: 25BOE10152**

**Course: Python Essentials**

**Project: BYOP (Bring Your Own Project)**

**Date: March 2026**

