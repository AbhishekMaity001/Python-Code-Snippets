import shutil
import time
import pandas as pd
import concurrent.futures
from datetime import datetime

# Change the variables path here
filename = 'births.csv'
source = 'births.csv'
destination = 'copy_births.csv'


class Calling_Program():
    def __init__(self, filename, source, destination):
        self.filename = filename
        self.source = source
        self.destination = destination

    def log(self, log_message):
        """
        This manual function is  used for logging purposes to track the status of the program
        :param log_message: The log message that needs to be written in the log file
        :return: None

        """
        with open('logger.txt', 'a+') as file :
            self.now = datetime.now()
            self.date = self.now.date()
            self.current_time = self.now.strftime("%H:%M:%S")
            file.write(str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message + "\n")
            file.close()


    def get_Data_File(self, filename):
        """
        This Function us used for Loading the file and fetching the meta data from it
        :param filename: the filename to be passed as an parameter
        :return: None
        """

        self.log("get_Data_File method Started....")
        self.filename = filename
        df = pd.read_csv(self.filename)
        time.sleep(1)  # Sleeping the function just for delay purposes
        self.log("get_Data_File method Finished")


    def move_File(self, source, destination):
        """
        This Function is used for copying the file from source to the destination
        :param source: Source file path
        :param destination: destination file path
        :return: None
        """
        self.source = source
        self.destination = destination
        self.log("move_File method Started.....")
        shutil.copy(source, destination)
        time.sleep(1)  # Sleeping the function just for delay purposes
        self.log("move_File method Finished")

    def job1(self):
        self.log("Job 1 method Started")
        time.sleep(3)
        self.log("Job 1 method Finished")

    def job2(self):
        self.log("Job 2 method Started")
        time.sleep(3)
        self.log("Job 2 method Finished")

    def job3(self):
        self.log("Job 3 method Started")
        time.sleep(3)
        self.log("Job 3 method Finished")


if __name__ == '__main__':  # main entry point of the Program
    start = time.perf_counter()
    open('logger.txt', 'w').close() # clearing the log file before starting the program
    print(".....Starting the Main Program.....")

    obj1 = Calling_Program(filename, source, destination)  # Creating object of Calling_Program()

    with concurrent.futures.ThreadPoolExecutor() as executor:

        executor.submit(obj1.get_Data_File(filename) )
        executor.submit(obj1.move_File(source, destination))

        # Starting Job1, Job2, Job3 concurrently
        executor.submit(obj1.job1)
        executor.submit(obj1.job2)
        executor.submit(obj1.job3)

    end = time.perf_counter()
    print("Total Executing time : {} seconds".format(end - start))



