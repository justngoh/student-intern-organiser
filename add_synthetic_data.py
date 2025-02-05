import sqlite3

def add_synthetic_project_data():
    conn = sqlite3.connect('student_intern_data/student_intern_data.db')
    cursor = conn.cursor()
    
    try:
        # First, check if we already have synthetic data
        cursor.execute("SELECT COUNT(*) FROM Students WHERE full_name LIKE 'Student%'")
        count = cursor.fetchone()[0]
        
        if count > 0:
            print("Synthetic data already exists. Skipping insertion to avoid duplicates.")
            return
            
        # Add projects if they don't exist
        projects = [
            ('REDMANE', 'active'),
            ('Clinical Dashboards', 'active'),
            ('Student Organiser', 'active'),
            ('Quantum Computing', 'active')
        ]
        
        for project in projects:
            cursor.execute('INSERT OR IGNORE INTO Projects (name, status) VALUES (?, ?)', project)
        
        # Add synthetic student data
        students_data = [
            # REDMANE (7 Science + 3 Engineering)
            *[('Student{}'.format(i), 'Science', 'REDMANE', 'current') for i in range(1, 8)],
            *[('Student{}'.format(i), 'Engineering and IT', 'REDMANE', 'current') for i in range(8, 11)],
            
            # Clinical Dashboards (10 Science + 8 Engineering)
            *[('Student{}'.format(i), 'Science', 'Clinical Dashboards', 'current') for i in range(11, 21)],
            *[('Student{}'.format(i), 'Engineering and IT', 'Clinical Dashboards', 'current') for i in range(21, 29)],
            
            # Student Organiser (10 Science + 10 Engineering)
            *[('Student{}'.format(i), 'Science', 'Student Organiser', 'current') for i in range(29, 39)],
            *[('Student{}'.format(i), 'Engineering and IT', 'Student Organiser', 'current') for i in range(39, 49)],
            
            # Quantum Computing (7 Science + 5 Engineering)
            *[('Student{}'.format(i), 'Science', 'Quantum Computing', 'current') for i in range(49, 56)],
            *[('Student{}'.format(i), 'Engineering and IT', 'Quantum Computing', 'current') for i in range(56, 61)]
        ]
        
        for student in students_data:
            cursor.execute('''
                INSERT OR IGNORE INTO Students 
                (full_name, course, project, status) 
                VALUES (?, ?, ?, ?)
            ''', student)
        
        conn.commit()
        print("Successfully added synthetic data!")
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    add_synthetic_project_data() 