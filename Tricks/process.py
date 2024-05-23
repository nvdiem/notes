import psutil
import time
import multiprocessing
import concurrent.futures
import requests

print(psutil.cpu_count())

def do_something():
    print('sleeping 1 second')
    time.sleep(1)
    print('done sleeping')
    
def do_something(t):
    print(f'sleeping {t} second(s)')
    time.sleep(t)
    print('done sleeping')


def get_isp_info():
    response = requests.get('http://ip-api.com/json/')
    data = response.json()
    return data['isp']    
        
if __name__ == '__main__':
    
    start = time.time()
    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # end = time.time()
    # print(f'finished in {round(end-start)} seconds')
    
    start = time.time()
    # with concurrent.futures.ProcessPoolExecutor() as ex:
    #     p1 = ex.submit(do_something, 1.5)
    #     p2 = ex.submit(do_something, 1.3)
        
    #     print(p1.result())
    #     print(p2.result())
    
    # end = time.time()
    # print(f'finished in {round(end-start)} seconds')




    # print(get_isp_info())

    # with concurrent.futures.ProcessPoolExecutor() as ex:
    #     secs = [5, 4, 3, 2, 1]
    #     results = ex.map(do_something, secs)
        
    #     for result in results:
    #         print(result)
            
    
    # end = time.time()
    # print(f'finished in {round(end-start)} seconds')
    
