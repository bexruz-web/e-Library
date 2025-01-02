# Vazifalarni saqlash uchun ro'yxat
tasks = []

# Vazifalarni ko'rish funksiyasi
def view_tasks():
    if not tasks:
        print("Vazifalar ro'yxati bo'sh.")
    else:
        print("\nVazifalar ro'yxati:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Yangi vazifa qo'shish funksiyasi
def add_task():
    title = input("Vazifa nomini kiriting: ")
    tasks.append(title)
    print("Vazifa muvaffaqiyatli qo'shildi!")

# Vazifani tahrirlash funksiyasi
def edit_task():
    view_tasks()
    try:
        task_no = int(input("Tahrirlamoqchi bo'lgan vazifa raqamini kiriting: "))
        if 1 <= task_no <= len(tasks):
            new_title = input("Yangi vazifa nomini kiriting: ")
            tasks[task_no - 1] = new_title
            print("Vazifa muvaffaqiyatli tahrirlandi!")
        else:
            print("Noto'g'ri raqam kiritildi.")
    except ValueError:
        print("Faqat raqam kiriting.")

# Vazifani o'chirish funksiyasi
def delete_task():
    view_tasks()
    try:
        task_no = int(input("O'chirmoqchi bo'lgan vazifa raqamini kiriting: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Vazifa muvaffaqiyatli o'chirildi!")
        else:
            print("Noto'g'ri raqam kiritildi.")
    except ValueError:
        print("Faqat raqam kiriting.")

# Vazifani tugallangan deb belgilash funksiyasi
def complete_task():
    view_tasks()
    try:
        task_no = int(input("Tugallangan deb belgilamoqchi bo'lgan vazifa raqamini kiriting: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1] += " [Tugallangan]"
            print("Vazifa tugallangan deb belgilandi!")
        else:
            print("Noto'g'ri raqam kiritildi.")
    except ValueError:
        print("Faqat raqam kiriting.")

# Asosiy menyu funksiyasi
def main_menu():
    while True:
        print("\nTo-do ro'yxati menyusi:")
        print("1. Vazifalarni ko'rish")
        print("2. Vazifa qo'shish")
        print("3. Vazifani tahrirlash")
        print("4. Vazifani o'chirish")
        print("5. Vazifani tugallangan deb belgilash")
        print("6. Chiqish")

        choice = input("Tanlovingizni kiriting: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            complete_task()
        elif choice == "6":
            print("Dastur tugatildi.")
            break
        else:
            print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")

# Dastur ishga tushiriladi
if __name__ == "__main__":
    main_menu()
