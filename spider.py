from urllib.request import urlopen
from link_finder import LinkFinder
from WebCrawler import *
import mysql.connector


#for using multithreading
class spider:
    
    # class variables for sharing variables among alla spiders
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()
    db_dict = {}


    def __init__(self, project_name , base_url , domain_name ) :
        spider.project_name = project_name
        spider.base_url = base_url
        spider.domain_name = domain_name
        spider.queue_file = spider.project_name + '/queue.txt'
        spider.crawled_file = spider.project_name + '/crawled.txt' 
        self.boot()
        self.crawl_page('First spider' , spider.base_url)


    #some functions that our first spider shall do
    @staticmethod   #vid10
    def boot():
        Create_project_dir(spider.project_name)
        create_date_files(spider.project_name , spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name , page_url):
        if page_url not in spider.crawled:
            
            #to show user that we are doing something
            print(thread_name + '  crawling ' + page_url)
            print('Queue '+ str(len(spider.queue)) + ' | Crawled ' + str(len(spider.crawled)))

            spider.add_links_to_queue(spider.gather_links(page_url))
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            spider.update_files()
            spider.update_db(page_url , spider.db_dict[page_url])

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in spider.queue:
                continue
            if url in spider.crawled:
                continue

            #if i dont use this here my crawler keeps on crawling for eternity
            if spider.domain_name not in url:
                continue
            spider.queue.add(url)



    @staticmethod
    def gather_links(page_url):
        html_string = ''
        #just because of the errors that can happen here
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf=8")


                title_start = html_string.find("title")
                title_end =  html_string.find("/title")

                spider.db_dict.update({ page_url : html_string[title_start + 6 : title_end - 1] })

            finder = LinkFinder(spider.base_url , page_url)
            finder.feed(html_string)

        except:
            print('error : can not crawl page')
            return set()

        return finder.page_links()


    @staticmethod
    def update_files():
        set_to_file(spider.queue , spider.queue_file)
        set_to_file(spider.crawled , spider.crawled_file)


    @staticmethod
    def update_db(db_url , db_title):
            
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ganji2130",
        database="mydatabase"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO urls (url, title) VALUES (%s, %s)"
        val = (db_url, db_title)
        mycursor.execute(sql, val)

        mydb.commit()




