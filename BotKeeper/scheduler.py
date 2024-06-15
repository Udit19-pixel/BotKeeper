import threading
import time

class Scheduler:
    def __init__(self):
        self.tasks = []
        self.lock = threading.Lock()
        self.cancel_event = threading.Event()

    def schedule_task(self, delay: int, task, args=()):
        run_time = time.time() + delay
        with self.lock:
            self.tasks.append((run_time, task, args))
            self.tasks.sort()

    def run(self):
        while not self.cancel_event.is_set():
            with self.lock:
                now = time.time()
                while self.tasks and self.tasks[0][0] <= now:
                    _, task, args = self.tasks.pop(0)
                    task(*args)
            time.sleep(0.1)

    def cancel_all_tasks(self):
        self.cancel_event.set()

    def __del__(self):
        self.cancel_all_tasks()