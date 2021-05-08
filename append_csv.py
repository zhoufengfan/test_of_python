def append(file_path, string):
    """
    Append data in csv file. If the file is not exist, the function will create the file.
    """
    f = open(file_path, "a")
    f.write(string)
    f.close()


if __name__ == '__main__':
    file_path = "D:/open_file_test.csv"
    # must add \n
    append(file_path, "0.1,2.5\n")
