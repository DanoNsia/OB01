class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Некорректный индекс задачи.")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def display_current_tasks(self):
        print("Текущие задачи:")
        for task in self.get_current_tasks():
            print(task)

    def display_all_tasks(self):
        print("Все задачи:")
        for task in self.tasks:
            print(task)


# Пример использования:
task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2023-11-01")
task_manager.add_task("Сделать домашнее задание", "2023-11-02")

print("Показать все задачи до выполнения:")
task_manager.display_all_tasks()

# Отметим первую задачу как выполненную
task_manager.mark_task_completed(0)

print("\nПоказать все задачи после выполнения:")
task_manager.display_all_tasks()

print("\nТекущие задачи:")
task_manager.display_current_tasks()