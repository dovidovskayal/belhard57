import threading
from time import sleep


def main():
    for i in range(1,11 ):




if __name__ == '__main__':
    threads = []
    for _ in range(10):
        threads.append(threading.Thread(target=main))
    for thread in threads:
        thread.start()