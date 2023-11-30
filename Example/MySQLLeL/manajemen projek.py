import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="pengelolaan_proyek"
)

# Function to display projects
def display_projects():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM proyek")
    projects = cursor.fetchall()
    for project in projects:
        print("Project ID:", project[0])
        print("Nama Proyek:", project[1])
        print("Tanggal Mulai:", project[2])
        print("Tanggal Selesai:", project[3])
        print()

# Function to add a project
def add_project():
    nama_proyek = input("Enter the project name: ")
    tanggal_mulai = input("Enter the start date (YYYY-MM-DD): ")
    tanggal_selesai = input("Enter the end date (YYYY-MM-DD): ")
    
    cursor = mydb.cursor()
    sql = "INSERT INTO proyek (nama_proyek, tanggal_mulai, tanggal_selesai) VALUES (%s, %s, %s)"
    val = (nama_proyek, tanggal_mulai, tanggal_selesai)
    cursor.execute(sql, val)
    mydb.commit()
    print("Project added successfully!")

# Function to update a project
def update_project():
    project_id = input("Enter the project ID: ")
    nama_proyek = input("Enter the updated project name: ")
    tanggal_mulai = input("Enter the updated start date (YYYY-MM-DD): ")
    tanggal_selesai = input("Enter the updated end date (YYYY-MM-DD): ")
    
    cursor = mydb.cursor()
    sql = "UPDATE proyek SET nama_proyek = %s, tanggal_mulai = %s, tanggal_selesai = %s WHERE id = %s"
    val = (nama_proyek, tanggal_mulai, tanggal_selesai, project_id)
    cursor.execute(sql, val)
    mydb.commit()
    print("Project updated successfully!")

# Function to delete a project
def delete_project():
    project_id = input("Enter the project ID: ")
    
    cursor = mydb.cursor()
    sql = "DELETE FROM proyek WHERE id = %s"
    val = (project_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Project deleted successfully!")

# Function to add a task
def add_task():
    id_proyek = input("Enter the project ID: ")
    nama_tugas = input("Enter the task name: ")
    tenggat_waktu = input("Enter the deadline (YYYY-MM-DD): ")
    
    cursor = mydb.cursor()
    sql = "INSERT INTO tugas (id_proyek, nama_tugas, tenggat_waktu) VALUES (%s, %s, %s)"
    val = (id_proyek, nama_tugas, tenggat_waktu)
    cursor.execute(sql, val)
    mydb.commit()
    print("Task added successfully!")

# Function to update a task
def update_task():
    task_id = input("Enter the task ID: ")
    nama_tugas = input("Enter the updated task name: ")
    tenggat_waktu = input("Enter the updated deadline (YYYY-MM-DD): ")
    
    cursor = mydb.cursor()
    sql = "UPDATE tugas SET nama_tugas = %s, tenggat_waktu = %s WHERE id = %s"
    val = (nama_tugas, tenggat_waktu, task_id)
    cursor.execute(sql, val)
    mydb.commit()
    print("Task updated successfully!")

# Function to delete a task
def delete_task():
    task_id = input("Enter the task ID: ")
    
    cursor = mydb.cursor()
    sql = "DELETE FROM tugas WHERE id = %s"
    val = (task_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Task deleted successfully!")

# Function to manage team
def manage_team():
    id_proyek = input("Enter the project ID: ")
    nama_anggota = input("Enter the team member name: ")
    posisi = input("Enter the team member position: ")
    
    cursor = mydb.cursor()
    sql = "INSERT INTO anggota_tim (id_proyek, nama_anggota, posisi) VALUES (%s, %s, %s)"
    val = (id_proyek, nama_anggota, posisi)
    cursor.execute(sql, val)
    mydb.commit()
    print("Team member added successfully!")

# Function to update team member
def update_team_member():
    member_id = input("Enter the team member ID: ")
    nama_anggota = input("Enter the updated team member name: ")
    posisi = input("Enter the updated team member position: ")
    
    cursor = mydb.cursor()
    sql = "UPDATE anggota_tim SET nama_anggota = %s, posisi = %s WHERE id = %s"
    val = (nama_anggota, posisi, member_id)
    cursor.execute(sql, val)
    mydb.commit()
    print("Team member updated successfully!")

# Function to delete team member
def delete_team_member():
    member_id = input("Enter the team member ID: ")
    
    cursor = mydb.cursor()
    sql = "DELETE FROM anggota_tim WHERE id = %s"
    val = (member_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Team member deleted successfully!")

# Function to display the menu
def display_menu():
    print("1. Display Projects")
    print("2. Add Project")
    print("3. Update Project")
    print("4. Delete Project")
    print("5. Add Task")
    print("6. Update Task")
    print("7. Delete Task")
    print("8. Manage Team")
    print("9. Update Team Member")
    print("10. Delete Team Member")
    print("0. Exit")

# Function to handle user input
def handle_input(choice):
    if choice == "1":
        display_projects()
    elif choice == "2":
        add_project()
    elif choice == "3":
        update_project()
    elif choice == "4":
        delete_project()
    elif choice == "5":
        add_task()
    elif choice == "6":
        update_task()
    elif choice == "7":
        delete_task()
    elif choice == "8":
        manage_team()
    elif choice == "9":
        update_team_member()
    elif choice == "10":
        delete_team_member()
    elif choice == "0":
        print("Exiting...")
    else:
        print("Invalid choice!")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (0-10): ")
    handle_input(choice)
    if choice == "0":
        break
