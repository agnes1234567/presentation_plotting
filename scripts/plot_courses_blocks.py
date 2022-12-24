import matplotlib.pyplot as plt
import json
import csv

def main():
    file_path = '../csv_tables/schedules.csv'
    schedule_data = []
    with open(file_path,'r') as data:
        for line in csv.reader(data):
            schedule_data.append(tuple([line[0],line[-2]]))
    schedule_data = list(filter(lambda x: x[1] != '', schedule_data[1:]))
    courses_by_blockid = {}
    for course, block in schedule_data:
        if block in courses_by_blockid:
            courses_by_blockid[block].append(course)
        else:
            courses_by_blockid[block] = [course]
    for block in courses_by_blockid:
        courses_by_blockid[block] = len(set(courses_by_blockid[block]))
    
    plt.figure('Courses by block')
    plt.title('Courses by block')
    plt.bar(courses_by_blockid.keys(), courses_by_blockid.values())
    plt.xlim(-1,len(courses_by_blockid.keys()))
    plt.legend()
    plt.gcf().set_size_inches(16, 8)
    #plt.show()
    
    block_id_name_map = {}
    with open('../csv_tables/blocks.csv','r') as data:
        for line in csv.reader(data):
            block_id_name_map[line[0]] = tuple([line[1],line[2]])
    block_id_name_map.pop('id')
    
    courses_by_block_name = {}
    for block in courses_by_blockid:
        block_name = (block_id_name_map[block][0] + ', ' + block_id_name_map[block][1])
        if block_name in courses_by_block_name:
            courses_by_block_name[block_name] += courses_by_blockid[block]
        else:
            courses_by_block_name[block_name] = courses_by_blockid[block]
    
    max_block_name_length = max([courses_by_block_name[block] for block in courses_by_block_name])
    print(max_block_name_length)
    courses_by_block_name_fullterm = {}
    courses_by_block_name_p1 = {}
    courses_by_block_name_p2 = {}
    
    for block in courses_by_block_name:
        try:
            int(block[0])
            try:
                int(block[-1])
                courses_by_block_name_fullterm[block] = courses_by_block_name[block]
            except:
                if(block[-1] == '-'):
                    courses_by_block_name_fullterm[block] = courses_by_block_name[block]
                else:
                    courses_by_block_name_p1[block[0]] = courses_by_block_name[block]
        except:
            courses_by_block_name_p2[block[-1]] = courses_by_block_name[block]

    
    plt.figure('Courses by block name, Fullterm')
    plt.bar(courses_by_block_name_fullterm.keys(), courses_by_block_name_fullterm.values())
    plt.xlim(-1,len(courses_by_block_name_fullterm.keys()))
    plt.ylim(0,max_block_name_length)
    plt.gcf().set_size_inches(16, 8.2)
    print(courses_by_block_name_fullterm)
    
    plt.figure('Courses by block name, Period 1')
    plt.bar(courses_by_block_name_p1.keys(), courses_by_block_name_p1.values())
    plt.xlim(-1,len(courses_by_block_name_p1.keys()))
    plt.ylim(0,max_block_name_length)
    plt.gcf().set_size_inches(16, 8.2)
    print(courses_by_block_name_p1)
    
    plt.figure('Courses by block name, Period 2')
    plt.bar(courses_by_block_name_p2.keys(), courses_by_block_name_p2.values())
    plt.xlim(-1,len(courses_by_block_name_p2.keys()))
    plt.ylim(0,max_block_name_length)
    plt.gcf().set_size_inches(16, 8.2)
    print(courses_by_block_name_p2)
    
    plt.show()
    
    
main()