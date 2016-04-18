
def get_data(file_name) :
    f = open(file_name)
    lines = f.readlines()
    lines.pop(0) # ignore headers
    data = []
    for line in lines:
        split_line = line.split(',')
        data.append([int(split_line[0]),split_line[1].strip('\r\n')])
    return data

def merge_to_csv(d, file_name) :
    f = open(file_name, 'w')
    f.write('ID,x,y\r\n')
    key_list = d.keys()
    key_list.sort()
    format_string = "%d,%s,%s\r\n"
    for key in key_list:
        f.write(format_string % (key,d[key][0], d[key][1]))

def removed_to_csv(d, var,file_name) :
    f = open(file_name, 'w')
    f.write('ID,%s\r\n' % var)
    key_list = d.keys()
    key_list.sort()
    format_string = "%d,%s\r\n"
    for key in key_list:
        f.write(format_string % (key,d[key]))

def main() :
    # Get lists of data from each file
    x_data = get_data("x.csv")
    y_data = get_data("y.csv")
    # Get IDs for each set of values
    x_ids = [x_data[i][0] for i in range(len(x_data))]
    y_ids = [y_data[i][0] for i in range(len(y_data))]
    # Create dictionaries out of each value list i.e. (ID : value)
    x_dict = {x[0]:x[1] for x in x_data}
    y_dict = {y[0]:y[1] for y in y_data}
    print "# values of X before removal: ", len(x_dict)
    print "# values of Y before removal: ", len(y_dict)
    # Find the missing IDs from each value set
    missing_x = []
    missing_y = []
    missing_both = []
    removed_x_dict = {}
    removed_y_dict = {}
    for i in range(max(x_ids)) :
        if (i + 1) not in x_ids :
            missing_x.append(i + 1)
    for i in range(max(y_ids)) :
        if (i + 1) not in y_ids :
            missing_y.append(i + 1)
    # Remove missing values from each value dictionary
    for i in missing_y :
        val = x_dict.pop(i,None)
        if val != None :
            removed_x_dict[i] = val
        else :
            missing_both.append(i)
    for i in missing_x :
        val = y_dict.pop(i,None)
        if val != None :
            removed_y_dict[i] = val
    for x in x_dict:
        if x not in y_dict:
            print x
    for y in y_dict:
        if y not in x_dict:
            print y
    
    print "# values of X after removal: ", len(x_dict)
    print "# values of Y after removal: ", len(y_dict)
    
    key_list = x_dict.keys()
    value_pairs = {key: (x_dict[key],y_dict[key]) for key in key_list}
    merge_to_csv(value_pairs, "xy.csv")

    print "Removed ID, Value Pairs of X"
    print "Number removed: ", len(removed_x_dict)
    x_kl = removed_x_dict.keys()
    x_kl.sort()
    for key in x_kl:
        print key, removed_x_dict[key]

    print "Removed ID, Value Pairs of Y"
    print "Number Removed: ", len(removed_y_dict)
    y_kl = removed_y_dict.keys()
    y_kl.sort()
    for key in y_kl :
        print key, removed_y_dict[key]

    print "IDs Missing From Both Sets of Data"
    print "Number Removed: ", len(missing_both)
    for i in missing_both:
        print i
    
    removed_to_csv(removed_x_dict, 'x', 'removed_x.csv')
    removed_to_csv(removed_y_dict, 'y', 'removed_y.csv')


if __name__ == "__main__" :
    main()