import matplotlib.pyplot as plt
import json

def plotter(file, str):
    plt.figure(str)
    plt.title(str)
    hist_dict = json.load(file)
    
    plt.bar(hist_dict.keys(), hist_dict.values())
    plt.xlim(-1,len(hist_dict.keys()) + 1)
    plt.legend()
    plt.gcf().set_size_inches(16, 8)

def main():
    file = open('./backup_data/block_hist.json', 'r')
    str = 'Histogram of blocks in combinations all'
    plotter(file, str)
    
    file = open('./backup_data/block_hist_fullterm.json', 'r')
    str = 'Histogram of blocks in combinations fullterm'
    plotter(file, str)
    
    file = open('./backup_data/block_hist_p1.json', 'r')
    str = 'Histogram of blocks in combinations period 1'
    plotter(file, str)
    
    file = open('./backup_data/block_hist_p2.json', 'r')
    str = 'Histogram of blocks in combinations period 2'
    plotter(file, str)
    plt.show()

main()