from threading import Thread, Lock, current_thread
from queue import Queue
import time

database_value = 0


def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f'In {current_thread().name} got {value}')
        q.task_done()


def increase():
    global database_value

    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":

    lock = Lock()

    print('Start value ', database_value)

    thread_1 = Thread(target=increase, args=(lock,))
    thread_2 = Thread(target=increase, args=(lock,))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print('End value ', database_value)

    # Queues
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(21766)
    first = q.get()
    print('queue ', first)
    q.task_done()
    # q.join()
    print('Queue empty ', q.empty())

    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

print('Completed ok')
