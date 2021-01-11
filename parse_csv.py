import csv

with open('sample data/names.csv','r')  as csvfile :

    csv_reader = csv.reader(csvfile)
    # next(csv_reader) # next() will just take out the first row of the object
    # next(csv_reader)
    # print(csv_reader) # this will only print the object of the csv.reader method
    with open('out.csv','w') as output :
        csv_writer = csv.writer(output,delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

with open('out.csv','r') as f:
    csv_reader = csv.DictReader(f,delimiter='\t')
    for line in csv_reader:
        print(line['first_name'])


#######################################################################################################


with open('sample data/names.csv','r') as file :
    csv_reader_object = csv.DictReader(file)

    with open('sample data/outp.csv','w') as fi :
        csv_writer_object = csv.DictWriter(fi,fieldnames=['first_name','last_name'])
        csv_writer_object.writeheader()

        for line in csv_reader_object:
            del line['email']
            csv_writer_object.writerow(line)
