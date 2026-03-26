"""
Quiz & Practice Test Generator
Subject-wise question bank with difficulty levels
"""


import random
import json
import os
from datetime import datetime

# ==================== CLASSES ====================

class Question:
    """Represents a single question with subject"""
    
    def __init__(self, text, options, correct_answer, subject, difficulty="medium"):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.subject = subject
        self.difficulty = difficulty
        self.times_asked = 0
        self.times_correct = 0
    
    def check_answer(self, user_answer):
        """Validate user's answer"""
        return user_answer.upper() == self.correct_answer.upper()
    
    def to_dict(self):
        """Convert to dictionary for storage"""
        return {
            'text': self.text,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'subject': self.subject,
            'difficulty': self.difficulty,
            'times_asked': self.times_asked,
            'times_correct': self.times_correct
        }


class Subject:
    """Represents a subject with its questions"""
    
    def __init__(self, name):
        self.name = name
        self.questions = []
    
    def add_question(self, question):
        self.questions.append(question)
    
    def get_questions_by_difficulty(self, difficulty):
        """Get questions filtered by difficulty"""
        return [q for q in self.questions if q.difficulty == difficulty]
    
    def get_stats(self):
        """Get statistics for this subject"""
        if not self.questions:
            return None
        
        total_asked = sum(q.times_asked for q in self.questions)
        total_correct = sum(q.times_correct for q in self.questions)
        
        return {
            'total_questions': len(self.questions),
            'total_attempts': total_asked,
            'accuracy': (total_correct / total_asked * 100) if total_asked > 0 else 0
        }


class QuizManager:
    """Manages all subjects and quiz operations"""
    
    def __init__(self):
        self.subjects = {}  # Dictionary: subject_name -> Subject object
    
    def add_subject(self, subject_name):
        """Add a new subject"""
        if subject_name not in self.subjects:
            self.subjects[subject_name] = Subject(subject_name)
            return True
        return False
    
    def add_question_to_subject(self, subject_name, question):
        """Add question to specific subject"""
        if subject_name in self.subjects:
            self.subjects[subject_name].add_question(question)
            return True
        return False
    
    def get_subject_names(self):
        """Get list of all subject names"""
        return list(self.subjects.keys())
    
    def get_questions_from_subject(self, subject_name, difficulty=None):
        """Get questions from a subject, optionally filtered by difficulty"""
        if subject_name not in self.subjects:
            return []
        
        if difficulty and difficulty != "mixed":
            return self.subjects[subject_name].get_questions_by_difficulty(difficulty)
        return self.subjects[subject_name].questions
    
    def get_questions_for_quiz(self, subject_name, num_questions, difficulty=None):
        """Get random questions for quiz"""
        questions = self.get_questions_from_subject(subject_name, difficulty)
        
        if len(questions) < num_questions:
            num_questions = len(questions)
        
        if num_questions == 0:
            return []
        
        return random.sample(questions, num_questions)
    
    def take_quiz(self, subject_name, num_questions, difficulty=None):
        """Conduct a quiz for a specific subject"""
        selected = self.get_questions_for_quiz(subject_name, num_questions, difficulty)
        
        if not selected:
            print(f"\n❌ No questions available for {subject_name}!")
            return None
        
        score = 0
        print(f"\n{'='*50}")
        print(f"QUIZ: {subject_name.upper()}")
        print(f"Questions: {len(selected)}")
        if difficulty and difficulty != "mixed":
            print(f"Difficulty: {difficulty.capitalize()}")
        print(f"{'='*50}\n")
        
        for idx, q in enumerate(selected, 1):
            print(f"\nQuestion {idx}/{len(selected)}")
            print(f"[Difficulty: {q.difficulty.upper()}]")
            print(f"\n{q.text}")
            print("\nOptions:")
            
            # Show options
            for i, opt in enumerate(q.options, 1):
                print(f"  {chr(64+i)}. {opt}")
            
            # Get user answer
            while True:
                answer = input("\nYour answer (A/B/C/D): ").strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    selected_option = q.options[ord(answer) - 65]
                    break
                print("Invalid! Enter A, B, C, or D")
            
            # Check answer
            q.times_asked += 1
            if q.check_answer(selected_option):
                score += 1
                q.times_correct += 1
                print("✅ Correct!")
            else:
                print(f"❌ Wrong! Correct answer: {q.correct_answer}")
            
            print(f"Score: {score}/{idx}")
        
        percentage = (score / len(selected)) * 100
        return {
            'subject': subject_name,
            'score': score,
            'total': len(selected),
            'percentage': percentage,
            'grade': self._get_grade(percentage)
        }
    
    def _get_grade(self, percentage):
        """Determine grade"""
        if percentage >= 90:
            return "A+ (Excellent!)"
        elif percentage >= 80:
            return "A (Very Good)"
        elif percentage >= 70:
            return "B (Good)"
        elif percentage >= 60:
            return "C (Satisfactory)"
        elif percentage >= 50:
            return "D (Needs Improvement)"
        else:
            return "F (Poor - Keep Practicing!)"
    
    def get_subject_stats(self):
        """Get statistics for all subjects"""
        stats = {}
        for name, subject in self.subjects.items():
            subject_stats = subject.get_stats()
            if subject_stats:
                stats[name] = subject_stats
        return stats


class User:
    """Tracks user progress"""
    
    def __init__(self, name):
        self.name = name
        self.quiz_history = []
    
    def add_result(self, result):
        self.quiz_history.append(result)
    
    def show_progress(self):
        """Display user progress"""
        if not self.quiz_history:
            print("\n📊 No quizzes taken yet!")
            return
        
        print(f"\n{'='*50}")
        print(f"PROGRESS REPORT - {self.name}")
        print(f"{'='*50}")
        print(f"Total Quizzes: {len(self.quiz_history)}")
        
        # Subject-wise breakdown
        subject_scores = {}
        for result in self.quiz_history:
            subject = result['subject']
            if subject not in subject_scores:
                subject_scores[subject] = []
            subject_scores[subject].append(result['percentage'])
        
        print("\n📚 Subject-wise Performance:")
        for subject, scores in subject_scores.items():
            avg = sum(scores) / len(scores)
            print(f"  {subject}: {avg:.1f}% average over {len(scores)} quizzes")
        
        # Latest quiz
        last = self.quiz_history[-1]
        print("\n📝 Latest Quiz:")
        print(f"  Subject: {last['subject']}")
        print(f"  Score: {last['score']}/{last['total']}")
        print(f"  Percentage: {last['percentage']:.1f}%")
        print(f"  Grade: {last['grade']}")


# ==================== DATA MANAGEMENT ====================

def save_data(manager):
    """Save all subjects and questions to file"""
    data = {}
    for subject_name, subject in manager.subjects.items():
        data[subject_name] = {
            'name': subject.name,
            'questions': [q.to_dict() for q in subject.questions]
        }
    
    with open('quiz_data.json', 'w') as f:
        json.dump(data, f, indent=2)

def load_data():
    """Load subjects and questions from file"""
    manager = QuizManager()
    
    try:
        with open('quiz_data.json', 'r') as f:
            data = json.load(f)
            
            # Check if data is a list (old format) or dict (new format)
            if isinstance(data, list):
                # Old format - convert to new format
                print("\n📝 Converting old question bank to subject-wise format...")
                manager.add_subject("General")
                
                for q_data in data:
                    q = Question(
                        q_data['text'],
                        q_data['options'],
                        q_data['correct_answer'],
                        "General",  # Default subject for old questions
                        q_data.get('difficulty', 'medium')
                    )
                    q.times_asked = q_data.get('times_asked', 0)
                    q.times_correct = q_data.get('times_correct', 0)
                    manager.add_question_to_subject("General", q)
                
                # Save in new format
                save_data(manager)
                print("✅ Conversion complete! Your old questions are now in 'General' subject.\n")
                
            elif isinstance(data, dict):
                # New format - load normally
                for subject_name, subject_data in data.items():
                    manager.add_subject(subject_name)
                    for q_data in subject_data['questions']:
                        q = Question(
                            q_data['text'],
                            q_data['options'],
                            q_data['correct_answer'],
                            q_data['subject'],
                            q_data['difficulty']
                        )
                        q.times_asked = q_data.get('times_asked', 0)
                        q.times_correct = q_data.get('times_correct', 0)
                        manager.add_question_to_subject(subject_name, q)
            
            return manager
            
    except FileNotFoundError:
        # No file exists - create default data
        print("\n📚 Creating new question bank...")
        create_default_data(manager)
        return manager
    except json.JSONDecodeError:
        # Corrupted file - create new data
        print("\n⚠️ Corrupted data file found. Creating new database...")
        create_default_data(manager)
        return manager

def create_default_data(manager):
    """Create default subjects and questions"""
    # Add subjects
    subjects = ['Python Basics', 'Data Structures', 'OOP', 'Databases']
    for subject in subjects:
        manager.add_subject(subject)
    
    # Python Basics Questions
    python_questions = [
        Question("What is the output of: print(type(10))",
                ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'list'>"],
                "<class 'int'>", "Python Basics", "easy"),
        
        Question("Which of the following is a mutable data type?",
                ["tuple", "string", "list", "int"],
                "list", "Python Basics", "easy"),
        
        Question("What is list comprehension?",
                ["Creating lists", "Deleting lists", "Copying lists", "Sorting lists"],
                "Creating lists", "Python Basics", "medium"),
    ]
    
    # Data Structures Questions
    ds_questions = [
        Question("Which data structure uses LIFO?",
                ["Queue", "Stack", "Array", "Linked List"],
                "Stack", "Data Structures", "easy"),
        
        Question("Which data structure uses FIFO?",
                ["Stack", "Tree", "Queue", "Graph"],
                "Queue", "Data Structures", "easy"),
        
        Question("What is the time complexity of binary search?",
                ["O(n)", "O(log n)", "O(n²)", "O(1)"],
                "O(log n)", "Data Structures", "hard"),
    ]
    
    # OOP Questions
    oop_questions = [
        Question("What does 'self' represent?",
                ["The class itself", "Current instance", "A special variable", "A method"],
                "Current instance", "OOP", "medium"),
        
        Question("What is inheritance?",
                ["Creating objects", "Hiding data", "Reusing code", "Overloading operators"],
                "Reusing code", "OOP", "medium"),
        
        Question("Which concept allows multiple forms?",
                ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"],
                "Polymorphism", "OOP", "hard"),
    ]
    
    # Databases Questions
    db_questions = [
        Question("What does SQL stand for?",
                ["Structured Query Language", "Simple Query Language", "System Query Language", "Standard Query Language"],
                "Structured Query Language", "Databases", "easy"),
        
        Question("Which command retrieves data?",
                ["INSERT", "UPDATE", "SELECT", "DELETE"],
                "SELECT", "Databases", "easy"),
        
        Question("What is a primary key?",
                ["Unique identifier", "Foreign key", "Duplicate key", "Composite key"],
                "Unique identifier", "Databases", "medium"),
    ]
    
    # Add all questions
    for q in python_questions:
        manager.add_question_to_subject("Python Basics", q)
    for q in ds_questions:
        manager.add_question_to_subject("Data Structures", q)
    for q in oop_questions:
        manager.add_question_to_subject("OOP", q)
    for q in db_questions:
        manager.add_question_to_subject("Databases", q)
    
    # Save initial data
    save_data(manager)


# ==================== MAIN PROGRAM ====================

def main():
    """Main program"""
    print("\n🎓 SUBJECT-WISE QUIZ GENERATOR")
    print("="*50)
    
    # Setup
    name = input("\nEnter your name: ") or "Student"
    user = User(name)
    manager = load_data()
    
    print(f"\n👋 Welcome, {name}!")
    print(f"📚 Available Subjects: {', '.join(manager.get_subject_names())}")
    
    while True:
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("1. Take Quiz")
        print("2. View Question Bank")
        print("3. Add New Subject")
        print("4. Add Question to Subject")
        print("5. Track Progress")
        print("6. View Subject Statistics")
        print("7. Exit")
        print("="*50)
        
        choice = input("\nSelect option (1-7): ")
        
        if choice == '1':
            # Take Quiz - Select Subject
            subjects = manager.get_subject_names()
            if not subjects:
                print("\n❌ No subjects available! Please add a subject first.")
                continue
            
            print("\n📚 SELECT SUBJECT")
            print("-"*30)
            for i, subject in enumerate(subjects, 1):
                print(f"{i}. {subject}")
            
            try:
                sub_choice = int(input("\nSelect subject number: "))
                if 1 <= sub_choice <= len(subjects):
                    selected_subject = subjects[sub_choice - 1]
                else:
                    print("Invalid selection!")
                    continue
            except ValueError:
                print("Invalid input!")
                continue
            
            # Number of questions
            print("\n📝 QUIZ SETUP")
            print("-"*30)
            
            # Get available questions count
            available = len(manager.get_questions_from_subject(selected_subject))
            if available == 0:
                print(f"\n❌ No questions available for {selected_subject}!")
                continue
            
            max_questions = min(10, available)
            print(f"Available questions: {available}")
            
            while True:
                try:
                    num = int(input(f"Number of questions (1-{max_questions}): "))
                    if 1 <= num <= max_questions:
                        break
                    print(f"Enter number between 1-{max_questions}")
                except ValueError:
                    print("Enter a valid number")
            
            # Difficulty level
            print("\n🎯 DIFFICULTY LEVEL")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            print("4. Mixed")
            diff_choice = input("Select (1-4): ")
            
            diff_map = {'1': 'easy', '2': 'medium', '3': 'hard', '4': 'mixed'}
            difficulty = diff_map.get(diff_choice, 'mixed')
            
            # Take quiz
            result = manager.take_quiz(selected_subject, num, difficulty if difficulty != 'mixed' else None)
            
            if result:
                print(f"\n{'='*50}")
                print("QUIZ RESULTS")
                print(f"{'='*50}")
                print(f"Subject: {result['subject']}")
                print(f"Final Score: {result['score']}/{result['total']}")
                print(f"Percentage: {result['percentage']:.1f}%")
                print(f"Grade: {result['grade']}")
                print(f"{'='*50}")
                
                user.add_result(result)
                save_data(manager)
                print("\n✅ Progress saved!")
        
        elif choice == '2':
            # View Question Bank
            subjects = manager.get_subject_names()
            if not subjects:
                print("\n📖 No subjects available!")
                continue
            
            print("\n📖 QUESTION BANK")
            print("="*60)
            
            for subject in subjects:
                questions = manager.get_questions_from_subject(subject)
                print(f"\n📚 {subject} ({len(questions)} questions)")
                print("-"*40)
                
                for idx, q in enumerate(questions, 1):
                    print(f"\n  {idx}. [{q.difficulty.upper()}] {q.text}")
                    print(f"     Options: {', '.join(q.options)}")
                    print(f"     Answer: {q.correct_answer}")
                    if q.times_asked > 0:
                        accuracy = (q.times_correct / q.times_asked) * 100
                        print(f"     📊 Success Rate: {accuracy:.1f}% ({q.times_correct}/{q.times_asked})")
        
        elif choice == '3':
            # Add New Subject
            print("\n➕ ADD NEW SUBJECT")
            print("-"*30)
            
            subject_name = input("Subject name: ").strip()
            if not subject_name:
                print("Subject name cannot be empty!")
                continue
            
            if manager.add_subject(subject_name):
                save_data(manager)
                print(f"\n✅ Subject '{subject_name}' added successfully!")
            else:
                print(f"\n❌ Subject '{subject_name}' already exists!")
        
        elif choice == '4':
            # Add Question to Subject
            subjects = manager.get_subject_names()
            if not subjects:
                print("\n❌ No subjects available! Please add a subject first.")
                continue
            
            print("\n📚 SELECT SUBJECT")
            print("-"*30)
            for i, subject in enumerate(subjects, 1):
                print(f"{i}. {subject}")
            
            try:
                sub_choice = int(input("\nSelect subject number: "))
                if 1 <= sub_choice <= len(subjects):
                    selected_subject = subjects[sub_choice - 1]
                else:
                    print("Invalid selection!")
                    continue
            except ValueError:
                print("Invalid input!")
                continue
            
            print(f"\n➕ ADD QUESTION TO {selected_subject.upper()}")
            print("-"*30)
            
            text = input("Question: ")
            
            print("\nOptions:")
            options = []
            for i in range(4):
                opt = input(f"Option {chr(65+i)}: ")
                options.append(opt)
            
            print("\nCorrect Answer:")
            for i, opt in enumerate(options):
                print(f"{chr(65+i)}. {opt}")
            
            while True:
                correct_letter = input("Enter correct option (A/B/C/D): ").upper()
                if correct_letter in ['A', 'B', 'C', 'D']:
                    correct_answer = options[ord(correct_letter) - 65]
                    break
                print("Invalid! Choose A, B, C, or D")
            
            print("\nDifficulty:")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            diff_choice = input("Select (1-3): ")
            diff_map = {'1': 'easy', '2': 'medium', '3': 'hard'}
            difficulty = diff_map.get(diff_choice, 'medium')
            
            # Create and add question
            new_q = Question(text, options, correct_answer, selected_subject, difficulty)
            manager.add_question_to_subject(selected_subject, new_q)
            save_data(manager)
            print("\n✅ Question added successfully!")
        
        elif choice == '5':
            # Track Progress
            print("\n📊 PROGRESS TRACKING")
            print("-"*30)
            user.show_progress()
        
        elif choice == '6':
            # View Subject Statistics
            stats = manager.get_subject_stats()
            if not stats:
                print("\n📊 No statistics available yet!")
                continue
            
            print("\n📊 SUBJECT STATISTICS")
            print("="*50)
            for subject, data in stats.items():
                print(f"\n📚 {subject}")
                print(f"   Total Questions: {data['total_questions']}")
                print(f"   Total Attempts: {data['total_attempts']}")
                print(f"   Overall Accuracy: {data['accuracy']:.1f}%")
        
        elif choice == '7':
            # Exit
            save_data(manager)
            print(f"\n👋 Goodbye, {name}!")
            print(f"📊 You've completed {len(user.quiz_history)} quizzes")
            print("Keep practicing! 🎓")
            break
        
        else:
            print("❌ Invalid option! Choose 1-7")

# ==================== RUN PROGRAM ====================

if __name__ == "__main__":
    main()