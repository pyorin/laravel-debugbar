import requests
from multiprocessing.dummy import Pool as ThreadPool

def checkDebug(site):
    try:
        r = requests.get(site)
        if 'PhpDebugBar' in r.text:
            print('[{}] > Vulnerable!'.format(site))
            saveres = open('result.txt', 'a')
            saveres.write(site+'\n')
        else:
            print('[{}] > Not Vulnerable!'.format(site))
    except:
        pass

print("Laravel Debugbar\nAuthor: angga1337\n")
site = open(input('Sitelist: '),'r').read().splitlines()
Thread = int(input('Thread: '))
pool = ThreadPool(Thread)
pool.map(checkDebug, site)
pool.close()
pool.join()
