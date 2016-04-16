def main() :
    d1 = {1 : 1.2, 2 : 3.5 , 4 : 3.5}
    d2 = {1 : 4.5, 2 : 6.7, 4 : 8.9}
    key_list = d1.keys()
    d_master = {key : (d1[key], d2[key]) for key in key_list}
    print d_master
    to_csv(d_master, 'test.csv')
def to_csv(d, file_name) :
    f = open(file_name, 'w')
    f.write('ID,x,y\r\n')
    key_list = d.keys()
    format_string = "%d,%f,%f\r\n"
    for key in key_list:
        f.write(format_string % (key,d[key][0], d[key][1]))

if __name__ == "__main__" :
    main()