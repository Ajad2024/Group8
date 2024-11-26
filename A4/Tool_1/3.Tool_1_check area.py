import pandas as pd


excel_file_path = r"C:\Users\ajads\Desktop\A-3-4\Check kind of space\ifcspace_With_Area.xlsx"
output_excel_path = r"C:\Users\ajads\Desktop\check_results.xlsx"


area_requirements = {
    "MEETING ROOM": 2.5,  # m2 person req.
    "OFFICE": 8.0,        
    "STUDENT":3.0,
    "Toilet": 5.0,        # fixed req(if you use fixed req. add belo this)
    "PRINTING": 3.0 ,      
    "AUDITORIUM":100
}


try:
    df = pd.read_excel(excel_file_path)
    print(f"Successfully loaded Excel file: {excel_file_path}")
except Exception as e:
    print(f"Failed to load Excel file: {e}")
    exit()


required_columns = ['LongName', 'Area']
if not all(col in df.columns for col in required_columns):
    print(f"Error: Excel file must contain the following columns: {required_columns}")
    exit()

# pass,comment
df['Status'] = 'Pass'
df['Comment'] = 'Congratulations'

# Check column
for index, row in df.iterrows():
    long_name = row['LongName']
    area = row['Area']
    
    for room_type, area_per_person in area_requirements.items():
        if room_type in long_name:
            try:
                if room_type in ["Toilet", "PRINTING", "AUDITORIUM"]:  # fixed area logic 
                    required_area = area_per_person
                    if area < required_area:                           #fail,comment
                        df.at[index, 'Status'] = 'Fail'
                        df.at[index, 'Comment'] = (
                            f"Required area for {room_type} is {required_area} m², "
                            f"but the available area is {area} m²."
                        )
                else:
                    # m2 logic
                    num_people = int(long_name.split()[-1].replace('P', ''))
                    required_area = num_people * area_per_person
                    if area < required_area:
                        df.at[index, 'Status'] = 'Fail'
                        df.at[index, 'Comment'] = (
                            f"Required area for {num_people}P in {room_type} is {required_area} m², "
                            f"but the available area is {area} m²."
                        )
            except ValueError:
                # fail,comment
                df.at[index, 'Status'] = 'Fail'
                df.at[index, 'Comment'] = "Invalid format for number of people."
            break  

# Save
try:
    df.to_excel(output_excel_path, index=False)
    print(f"Results saved to Excel file: {output_excel_path}")
except Exception as e:
    print(f"Failed to save Excel file: {e}")
