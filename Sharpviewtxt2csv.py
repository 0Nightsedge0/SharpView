import sys
import csv
import itertools

print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv))

def main(argv):
    if(len(argv) != 3 or argv[1] == "-help" or argv[1] == "-h" or argv[1] == "--help"):
        print("Usage:")
        print("python Sharpviewtxt2csv.py <-h> source.txt output.csv")
        exit()
    else:
        sourcetxtpath = argv[1]
        outputcsvpath = argv[2]

    csv_dict_array = []
    csv_dict = {}
    with open(sourcetxtpath, encoding="UTF-8") as f:
            for line in f:
                # print(line.strip())
                if line not in ['\n', '\r\n']:
                    key, value = line.replace(" ", "").replace("\n", "").split(":", 1)
                    # print(key, value)
                    csv_dict[key] = value
                else:
                    csv_dict_array.append(csv_dict)
                    csv_dict = {}
    # print(csv_dict_array)
    
    # confirm cols
    cols = []
    cols = list(csv_dict_array[0].keys())
    for csv_dict_array_list in csv_dict_array:
        for csv_dict_array_list_item in csv_dict_array_list:
            if csv_dict_array_list_item not in cols:
                cols.append(csv_dict_array_list_item)
    # print(cols)

    # ensure all cols
    for csv_dict_array_item in csv_dict_array:
        for cols_item in cols:
            if cols_item not in csv_dict_array_item:
                # print(csv_dict_array_item, cols_item)
                csv_dict_array_item.update({cols_item: ""})
    # print(csv_dict_array)
    
    # output csv
    with open(outputcsvpath, "w", newline="\n", encoding="UTF-8") as wf:
        wdwrter = csv.DictWriter(wf, csv_dict_array[0].keys())
        wdwrter.writeheader()
        wdwrter.writerows(csv_dict_array)

main(sys.argv)