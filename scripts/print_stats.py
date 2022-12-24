import json
import csv
import math

def main():
    file = '../csv_tables/schedules.csv'
    ids = []
    block_ids = []
    with open(file,'r') as data:
        for line in csv.reader(data):
            if line[-2] != '' and line[-2] != 'ht-23':
                ids.append(line[0])
                block_ids.append(line[-2])
    
    print(len(set(ids)))
    print(len(block_ids))

    file = '../csv_tables/hpmap.csv'
    hp_stats = {}
    with open(file,'r') as data:
        for line in csv.reader(data):
            if line[0] in ids:
                if line[1] in hp_stats:
                    hp_stats[line[1]] += 1
                else:
                    hp_stats[line[1]] = 1
    for hp in hp_stats:
        print(hp + ': ' + str(round(hp_stats[hp]/len(ids), 4)*100))
        
    file = '../csv_tables/blocks.csv'
    block_map = {}
    
    with open(file,'r') as data:
        for line in csv.reader(data):
            if line[0] in block_ids:
                val = line[1] + ', ' + line[2]
                block_map[line[0]] = val
    
    fullterm_by_blocks = []
    period1_by_blocks = []
    period2_by_blocks = []
    
    for block_id in block_ids:
        val = block_map[block_id]
        try:
            int(val[0])
            try:
                int(val[-1])
                fullterm_by_blocks.append(val)
            except:
                if(val[-1] == '-'):
                    fullterm_by_blocks.append(val)
                else:
                    period1_by_blocks.append(val[0])
        except:
            period2_by_blocks.append(val[-1])
    
    
    fullterm_by_blocks_stats = {}
    period1_by_blocks_stats = {}
    period2_by_blocks_stats = {}
    
    for block in fullterm_by_blocks:
        if block in fullterm_by_blocks_stats:
            fullterm_by_blocks_stats[block] += 1
        else:
            fullterm_by_blocks_stats[block] = 1
            
    for block in period1_by_blocks:
        if block in period1_by_blocks_stats:
            period1_by_blocks_stats[block] += 1
        else:
            period1_by_blocks_stats[block] = 1
    
    for block in period2_by_blocks:
        if block in period2_by_blocks_stats:
            period2_by_blocks_stats[block] += 1
        else:
            period2_by_blocks_stats[block] = 1
    
    print(fullterm_by_blocks_stats)
    print(period1_by_blocks_stats)
    print(period2_by_blocks_stats)
    
    
    sched_type_stats = {'fullterm': 0, 'p1': 0, 'p2': 0}
    
    for key in fullterm_by_blocks_stats:
        sched_type_stats['fullterm'] += fullterm_by_blocks_stats[key]
    
    for key in period1_by_blocks_stats:
        sched_type_stats['p1'] += period1_by_blocks_stats[key]
    
    for key in period2_by_blocks_stats:
        sched_type_stats['p2'] += period2_by_blocks_stats[key]
    
    total = 0
    for key in fullterm_by_blocks_stats:
        total += calc_combination_count(key, period1_by_blocks_stats, period2_by_blocks_stats) \
            * fullterm_by_blocks_stats[key]
    
    print(total)
    print(sched_type_stats)
    

def calc_combination_count(fullterm_key, p1, p2):
    p1_key = fullterm_key[0]
    p2_key = fullterm_key[-1]
    p1_vals_to_combine = []
    for key in p1:
         if key != p1_key:
            p1_vals_to_combine.append(p1[key])
            
    p2_vals_to_combine = []
    for key in p2:
        if key != p2_key:
            p2_vals_to_combine.append(p2[key])
            
    return recursive_combination_prod(0, p1_vals_to_combine) * recursive_combination_prod(0, p2_vals_to_combine)
    
def recursive_combination_prod(res, lst):
    if(len(lst) == 0):
        return res
    else:
        res += lst[0] * sum(lst[1:])
        return recursive_combination_prod(res, lst[1:])


main()