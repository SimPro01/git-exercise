#%%
# Reading and interpreting DICOM files using pydicom library

# Import necessary libraries after installing them into the virtual environment "skills"
import pydicom
import matplotlib.pyplot as plt

#%%
# Read a DICOM file, create a function
def read_dicom_file(file_path):
    dataset = pydicom.dcmread(file_path)
    
    # Access specific attributes
    patient_name = dataset.PatientName
    patient_id = dataset.PatientID
    study_date = dataset.StudyDate

    # Replace '^' with space in patient name for better readability
    patient_name = str(patient_name).replace('^', ' ')

    # Change the date formatting to a more readable format (DD-MM-YYYY)
    study_date = f"{study_date[6:8]}-{study_date[4:6]}-{study_date[0:4]}"

    # Print the information
    print(patient_name)
    print(patient_id)
    print(study_date)

# Call the function
read_dicom_file("/Users/sima/Downloads/MIE2003/git-exercise/Dataset_Skills_01/CT/1.3.12.2.1107.5.1.4.105055.30000018070216565044500079806/1.3.12.2.1107.5.1.4.105055.30000018070216565044500079807.dcm")

#%%
# Display the DICOM image using matplotlib
def display_dicom_image(file_path):
    dataset = pydicom.dcmread(file_path)
    
    # Extract pixel data
    pixel_array = dataset.pixel_array
    
    # Display the image
    plt.imshow(pixel_array, cmap=plt.cm.gray)
    plt.title('DICOM Image')
    plt.axis('off')  # Hide axis
    plt.show()

# Call the function
display_dicom_image("/Users/sima/Downloads/MIE2003/git-exercise/Dataset_Skills_01/CT/1.3.12.2.1107.5.1.4.105055.30000018070216565044500079806/1.3.12.2.1107.5.1.4.105055.30000018070216565044500079807.dcm")
#%%
# Explore the Metadata of the DICOM file
def explore_dicom_metadata(file_path):
    dataset = pydicom.dcmread(file_path)
    
    # Print all metadata attributes
    print("DICOM Metadata:")
    for elem in dataset:
        print(f"{elem.tag} : {elem.name} = {elem.value}")

# Call the function
explore_dicom_metadata("/Users/sima/Downloads/MIE2003/git-exercise/Dataset_Skills_01/CT/1.3.12.2.1107.5.1.4.105055.30000018070216565044500079806/1.3.12.2.1107.5.1.4.105055.30000018070216565044500079807.dcm")
#%%




