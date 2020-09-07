# -----------------------------------------------------------#
# Title: TestHarness.py
# Description: A Script to test modules successively as they are added
# ChangeLog:
#   GBiehl, 09.03.2020, Import Person and Processing Classes
#       Add code to test reading and writing to PersonData.txt
#   GBiehl, 09.04.2020, Add code to test reading and writing to EmployeeData
#   GBiehl, 09.05.2020, Added while loop to process menu choices
# ---------------------------------------------------------- #
# Harness script begins
#
# Be sure we are not in one of the modules
if __name__ == "__main__":
    from DataClasses import Person as P   # Trying out using aliases
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as FP
    from IOClasses import EmployeeIO as EmpIO
else:
    raise Exception("This file was not created to be imported")

# Test reading PersonData.txt and Processor Class
print ('Test reading PersonData file')
lstFileData = FP.read_data_from_file("PersonData.txt")
lstTable = []
for line in lstFileData:
    lstTable.append(P(line[0], line[1].strip()))
for row in lstTable:
    print(row.to_string())

# Test writing to PersonData.txt
FP.save_data_to_file("PersonData.txt", lstTable)
print ('Writing to and reading back from PersonData file')
lstFileData = FP.read_data_from_file("PersonData.txt")  # Read back to check
lstTable.clear()
for line in lstFileData:
    lstTable.append(P(line[0], line[1].strip()))
for row in lstTable:
    print(row.to_string())
print('The above listings should be the same \n')
#
# Test Employee class
print ('Test reading EmployeeData file')
lstFileData = FP.read_data_from_file("EmployeeData.txt")
lstTable = []
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string())

# Test writing to PersonData.txt
FP.save_data_to_file("EmployeeData.txt", lstTable)
print ('Writing to and reading back from EmployeeData file')
lstFileData = FP.read_data_from_file("EmployeeData.txt")  # Read back to check
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string())
print('The above listings should be the same \n')
#
# Test IO class
booContinue = True
while booContinue == True:
    EmpIO.print_menu_items()
    strChoice = EmpIO.input_menu_options()
    if strChoice == '1':
        for row in lstTable:
            print(row.to_string())
    elif strChoice == '2':
        NewEmp = []
        NewEmp = EmpIO.input_employee_data()
        lstTable.append(NewEmp)
        for row in lstTable:
            print(row.to_string())
    elif strChoice == '3':
        FP.save_data_to_file("EmployeeData.txt", lstTable)
    elif strChoice == '4':
        booContinue = False
# While loop ends
print('Goodby')
exit()