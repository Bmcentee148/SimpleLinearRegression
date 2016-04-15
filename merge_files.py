
def get_data(file_name) :
    f = open(file_name)
    lines = f.readlines()
    lines.pop(0)
    data = []
    for line in lines:
        split_line = line.split(',')
        data.append([int(split_line[0]),float(split_line[1])])
    return data

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
    # Find the missing IDs from each value set
    missing_x = []
    missing_y = []
    missing_x_dict = {}
    missing_y_dict = {}
    for i in range(max(x_ids)) :
        if (i + 1) not in x_ids :
            missing_x.append(i + 1)
    for i in range(max(y_ids)) :
        if (i + 1) not in y_ids :
            missing_y.append(i + 1)
    # Remove missing values from each value dictionary
    for i in missing_y :
        x_dict.pop(i,None)
    for i in missing_x :
        y_dict.pop(i,None)
    for x in x_dict:
        if x not in y_dict:
            print x
    for y in y_dict:
        if y not in x_dict:
            print y
    for x in missing_x_dict :
        print x

    print x_dict
    print '-' * 10
    print y_dict
    # for i in range(max(max(x_ids,max(y_ids)))) :
    #     print i
    # for point in x_data:
    #     print point
    # for point in y_data:
    #     print point

if __name__ == "__main__" :
    main()