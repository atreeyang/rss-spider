from multiprocessing import Process, Pipe
import time, os, sched

def f(conn):
    i = 0
    while True:
        i = i + 1
        conn.send(i)
        print(i)
        if(i == 5):
            conn.send(0)
        time.sleep(1)
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    while True:
        if(parent_conn.recv() == 0):
            p.terminate()
            break
    p.join()
    print("termate")
