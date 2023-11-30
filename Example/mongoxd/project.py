import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["project_management"]
projects_collection = db["projects"]

# Check if the database already exists
if "projects" not in db.list_collection_names():
    # Create the projects collection
    projects_collection = db.create_collection("projects")

# CRUD operations
def create_project():
    name = input("Enter project name: ")
    description = input("Enter project description: ")
    project = {"name": name, "description": description}
    projects_collection.insert_one(project)
    print("Project created successfully!")

def read_projects():
    projects = projects_collection.find()
    for project in projects:
        print(f"Name: {project['name']}, Description: {project['description']}")

def update_project():
    project_name = input("Enter project name to update: ")
    new_description = input("Enter new project description: ")
    query = {"name": project_name}
    new_values = {"$set": {"description": new_description}}
    projects_collection.update_one(query, new_values)
    print("Project updated successfully!")

def delete_project():
    project_name = input("Enter project name to delete: ")
    query = {"name": project_name}
    projects_collection.delete_one(query)
    print("Project deleted successfully!")

# Dynamic menu
def show_menu():
    print("===== Project Management Menu =====")
    print("1. Create Project")
    print("2. Read Projects")
    print("3. Update Project")
    print("4. Delete Project")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

# Main program
def main():
    while True:
        choice = show_menu()
        if choice == "1":
            create_project()
        elif choice == "2":
            read_projects()
        elif choice == "3":
            update_project()
        elif choice == "4":
            delete_project()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
