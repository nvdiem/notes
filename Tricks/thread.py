import threading
import time
import concurrent.futures

# def doing_something():
#     print('doing something')
#     time.sleep(1)
#     print('done doing something')    
    
# start = time.time() #get the current time
# doing_something()
# doing_something()
# end = time.time() #get the current time

# print(f'finished in {end-start} seconds')


def doing_something():
    print('doing something')
    time.sleep(1)
    print('done doing something')
    
#using threading
start = time.time() #get the current time
thread1 = threading.Thread(target=doing_something)
thread2 = threading.Thread(target=doing_something)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
end = time.time() #get the current time

print(f'finished in {round(end-start)} seconds')

threads = []

# start = time.time()
# for _ in range(10):
#     thread = threading.Thread(target=doing_something)
#     thread.start()
#     threads.append(thread)
    
# for thread in threads:
#     thread.join()
    
# end = time.time()

print(f'finished in {round(end-start)} seconds')
    
def do_something(t1, t2):
    seconds = t1 + t2
    print(f'sleeping {seconds} second(s)')
    time.sleep(seconds)
    print('done sleeping')

# start = time.time()
# with concurrent.futures.ThreadPoolExecutor() as ex:
#     f1 = ex.submit(do_something, 1, 0.5)
#     f2 = ex.submit(do_something, 1, 0.5)
#     f3 = ex.submit(do_something, 1, 0.5)
#     print(f1.result())
#     print(f2.result())
#     print(f3.result())
# end = time.time()
# print(f'finished in {round(end-start)} seconds')

start = time.time()
def do_something(t):
    print(f'sleeping {t} second(s)')
    time.sleep(t)
    return 'done sleeping'

with concurrent.futures.ThreadPoolExecutor() as ex:
    secs = [5, 4, 3, 2, 1]
    results = ex.map(do_something, secs)

    for result in results:
        print(result)
end = time.time()
print(f'finished in {round(end-start)} seconds')