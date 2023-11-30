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

# Function to add a task
def add_task(id_proyek, nama_tugas, tenggat_waktu):
    cursor = mydb.cursor()
    sql = "INSERT INTO tugas (id_proyek, nama_tugas, tenggat_waktu) VALUES (%s, %s, %s)"
    val = (id_proyek, nama_tugas, tenggat_waktu)
    cursor.execute(sql, val)
    mydb.commit()
    print("Task added successfully!")

# Function to manage team
def manage_team(id_proyek, nama_anggota, posisi):
    cursor = mydb.cursor()
    sql = "INSERT INTO anggota_tim (id_proyek, nama_anggota, posisi) VALUES (%s, %s, %s)"
    val = (id_proyek, nama_anggota, posisi)
    cursor.execute(sql, val)
    mydb.commit()
    print("Team member added successfully!")

# Call the functions
display_projects()
add_task(1, "Task 1", "2022-01-01")
manage_team(1, "John Doe", "Developer")
