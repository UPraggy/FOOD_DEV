# Summary
- **[Objective]()**
- **[List Functions]()**
- **[Functions]()**
# Objective
- The objective of this module is to perform the basic operations of
include, select, update and delete.
The other functions aim to simplify and improve performance and
visualization, trying to escape the repetition of lines.

# List Functions
- [Insert Data ]()
- [Select Data ]()
- [Update Data ]()
- [Delete Data ]()
- [Verify Type ]()
- [Search Data ]()

# Functions

## Insert Data
The structure has as entries the file_path which varies according to
the type_data which is the other input, its purpose is to insert data in the selected file.<br>
- Entries:<br>
   - Type_data -> input variable that checks what type of file
     that you want to access "CLIENT" or "ORDER". Its function is to help the File_path.

  - File_path -> input variable that receives the folder address
    where the file is located, varying according to the Type_data. When the
    Type_data assumes "ORDER" it receives the address of the Verify_type function where the
    set of operations around directories and files. When it assumes "CLIENT"
    it doesn't need to go through the conditional structure as it already has a directory
    default, which was received.
    Obs.: When assuming the value "ORDER" the variable also has other parameters of which
    are used in the Verify_type function, the description about these entries will be in the
    Verify_Type function description

- Operation:
  - After setting the value of File_path, the open operation is performed
    the excel file through Pandas and storage in the Data variable
    
  - stored the columns in the Cols variable

  - Creation of an Nw_data vector that will receive the input data
    it was created to the exact size according to the columns.
    
  - After creating the vector and inputting data the vector is converted
    in a tuple which is the only way to create a Data_frame
    as seen soon after
    
  - The Data variable receives as a vector it and the new dataframe for logo
    then join the data with the concatenate function into a single DataFrame
    
  - Finally, the index is set for the first column of data so that
  the first column of the new DataFrame does not display the column index values
  as 0,1,2... and yes as the first column, after that the saving is done
of the data file with all changes in excel format.
