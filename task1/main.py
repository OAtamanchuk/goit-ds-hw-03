from pymongo import MongoClient
from pymongo.errors import PyMongoError
from pymongo.server_api import ServerApi

# Підключення до MongoDB
MONGO_URI = "mongodb+srv://aleksa_db_user:41aA2EiScayTWvXg@cluster0.ig9pt9q.mongodb.net/"
client = MongoClient(MONGO_URI, server_api=ServerApi("1"))
db = client.cats_db        # назва бази
cats = db.cats_collection  # назва колекції

# CREATE
def add_cat(name, age, features):
    # Додає нового кота в колекцію
    try:
        result = cats.insert_one({
            "name": name,
            "age": age,
            "features": features
        })
        print(f"Cat added with id {result.inserted_id}")
    except PyMongoError as e:
        print("Error while inserting:", e)

# READ
def show_all_cats():
    # Показує всі записи у колекції
    try:
        all_cats = list(cats.find())
        if not all_cats:
            print("Collection is empty.")
            return
        for cat in all_cats:
            print(cat)
    except PyMongoError as e:
        print("Error while reading:", e)

def find_cat_by_name(name):
    # Показує інформацію про кота за ім'ям
    try:
        result = cats.find_one({"name": name})
        if result:
            print(result)
        else:
            print("Cat not found.")
    except PyMongoError as e:
        print("Error while reading:", e)

# UPDATE
def update_cat_age(name, new_age):
    # Оновлює вік кота за ім'ям
    try:
        result = cats.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count:
            print("Age updated.")
        else:
            print("No cat updated. Name not found.")
    except PyMongoError as e:
        print("Error while updating:", e)

def add_feature(name, new_feature):
    # Додає нову рису коту за ім'ям
    try:
        result = cats.update_one(
            {"name": name},
            {"$push": {"features": new_feature}}
        )
        if result.modified_count:
            print("Feature added.")
        else:
            print("No cat updated. Name not found.")
    except PyMongoError as e:
        print("Error while updating:", e)

# DELETE
def delete_cat(name):
    # Видаляє кота за ім'ям
    try:
        result = cats.delete_one({"name": name})
        if result.deleted_count:
            print("Cat deleted.")
        else:
            print("Cat not found.")
    except PyMongoError as e:
        print("Error while deleting:", e)

def delete_all():
    # Видаляє всіх котів з колекції
    try:
        cats.delete_many({})
        print("All cats deleted.")
    except PyMongoError as e:
        print("Error while deleting:", e)


def print_menu():
    print("     CATS DATABASE     ")
    print("Available commands:")
    print(" 1 - Add new cat")
    print(" 2 - Show all cats")
    print(" 3 - Find cat by name")
    print(" 4 - Update cat age")
    print(" 5 - Add new feature")
    print(" 6 - Delete cat")
    print(" 7 - Delete ALL cats")
    print(" 0 - Exit\n")

def run_menu():
    while True:
        choice = input("Enter command: ").strip()

        if choice == "1":
            name = input("Enter cat name: ").strip()
            age = input("Enter age: ").strip()

            if not age.isdigit():
                print("Age must be a number!")
                continue

            features = input("Enter features (comma separated): ").split(",")
            features = [f.strip() for f in features if f.strip()]

            add_cat(name, int(age), features)

        elif choice == "2":
            show_all_cats()

        elif choice == "3":
            name = input("Enter name: ").strip()
            find_cat_by_name(name)

        elif choice == "4":
            name = input("Enter name: ").strip()
            age = input("Enter new age: ")

            if not age.isdigit():
                print("Age must be a positive number!")
                continue

            update_cat_age(name, int(age))

        elif choice == "5":
            name = input("Enter name: ").strip()
            feature = input("Enter new feature: ").strip()
            add_feature(name, feature)

        elif choice == "6":
            name = input("Enter name: ").strip()
            delete_cat(name)

        elif choice == "7":
            confirm = input("Are you sure? Type YES to confirm: ")
            if confirm.strip().lower() == "yes":
                delete_all()
            else:
                print("Cancelled.")

        elif choice == "0":
            print("Goodbye! ")
            break

        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    print_menu()
    run_menu()