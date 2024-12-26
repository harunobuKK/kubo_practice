import os

TODO_DIR = "todos"
TODO_FILE = os.path.join(TODO_DIR, "todo1.txt")
COMPLETED_FILE = os.path.join(TODO_DIR, "completed.txt")

# 初期設定
os.makedirs(TODO_DIR, exist_ok=True)
open(TODO_FILE, 'a').close()
open(COMPLETED_FILE, 'a').close()

def add_task(task):
    with open(TODO_FILE, 'a') as f:
        f.write(task + "\n")
    print(f"タスクを追加しました: {task}")

def list_tasks():
    print("現在のタスク:")
    with open(TODO_FILE, 'r') as f:
        tasks = f.readlines()
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")

def complete_task(task_number):
    with open(TODO_FILE, 'r') as f:
        tasks = f.readlines()
    if task_number < 1 or task_number > len(tasks):
        print("無効なタスク番号です")
        return
    task = tasks.pop(task_number - 1)
    with open(TODO_FILE, 'w') as f:
        f.writelines(tasks)
    with open(COMPLETED_FILE, 'a') as f:
        f.write(task)
    print(f"タスクを完了しました: {task.strip()}")

def main():
    while True:
        print("\nTODOアプリ - 選択肢")
        print("1: タスクを追加")
        print("2: タスク一覧を表示")
        print("3: タスクを完了にする")
        print("4: 終了")
        choice = input("選択してください: ")
        
        if choice == "1":
            task = input("追加するタスクを入力してください: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            task_number = int(input("完了にするタスク番号を入力してください: "))
            complete_task(task_number)
        elif choice == "4":
            print("終了します")
            break
        else:
            print("無効な選択です。再試行してください。")

if __name__ == "__main__":
    main()
