import os


#create folders for better finding
def Create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating => ' + directory)
        os.makedirs(directory)


#create queue and crawled files
def create_date_files(project_name , base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#create a new file 
def write_file(path , data):
    f= open(path , 'w')
    f.write(data)
    f.close()



#add data onto an existing file
def append_data(path , data):
    with open(path , 'a' , encoding='utf-8') as file :
        file.write(data+ '\n')


#delete contents of a file
def delete_file_contents(path):
    with open(path , 'w'):
        pass

#file to set
def file_to_set (file_name):
    results = set()
    with open(file_name, 'rt' , encoding='utf-8') as f:
        for line in f:
            results.add(line.replace('\n', '')) #cause we used \n for each line
    return results


#itrate through a set and items will be a new line in file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_data(file, link)





