import queue
import threading
from queue import Queue
from spider import *
from WebCrawler import *
from domain import *


PROJECT_NAME = 'w3schools'
HOME_PAGE = 'https://www.w3schools.com/default.asp'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE =  PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
thread_queue = Queue()
spider(PROJECT_NAME , HOME_PAGE , DOMAIN_NAME)


#create worker threads (will die if main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t= threading.Thread(target=work)
        t.daemon = True
        t.start()


#do the next job
def work():
    while True:
        url = thread_queue.get()
        spider.crawl_page(threading.current_thread().name , url)
        thread_queue.task_done()


#Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        thread_queue.put(link)
    thread_queue.join()
    crawl()


#check if there are items in the queue if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0 :
        print(str(len(queued_links)) + ' links in  the queue! \n')
        create_jobs()

create_workers()
crawl()