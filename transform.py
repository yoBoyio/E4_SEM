import pandas as pd

# Define the Excel file path
file_path = '1.xlsx'  # Make sure to update this with the correct file path

# Define the sheet names for groups A to C (extend this list for more groups as needed)
sheet_names = ['A', 'B', 'C', 'D']


# Initialize an empty DataFrame to store aggregated results from all groups
all_groups_data = pd.DataFrame()

# Process data for each group
for sheet_name in sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Initialize an empty DataFrame for this group
    # group_data = pd.DataFrame()
    print(df)
    # # Process data for each case using the specific case beginnings for the current group
    # for case_number, beginning_string in case_beginnings.items():
    #     relevant_columns = [col for col in df.columns if col.startswith(beginning_string)]
    #     confidence_column = f"{beginning_string[:-1]}.1_1"  # Updated to fetch confidence level
    #     time_start_column = f"{beginning_string[:-7]} Timing1_First Click"
    #     time_end_column = f"{beginning_string[:-7]} Timing1_Last Click"
    #     # print(time_start_column)  
    #     case_data = df[relevant_columns + [confidence_column] + [time_start_column] + [time_end_column]]  # Include confidence column in the case data
    #     # print(confidence_column)
    #     # Simplify the column names
    #     simplified_columns = {col: f"{i+1}" for i, col in enumerate(relevant_columns)}
    #     case_data = case_data.rename(columns=simplified_columns)

    #     # Identify the exact columns marked as "On" and "Off" for each participant in this case
    #     for i in range(1, case_data.shape[0]):  # Assuming first row is header/description
    #         on_columns = [col for col, value in case_data.iloc[i].items() if value == "On"]
    #         off_columns = [col for col, value in case_data.iloc[i].items() if value == "Off"]
    #         confidence_level = df.loc[i, confidence_column]
    #         time_start = df.loc[i, time_start_column]
    #         time_end = df.loc[i, time_end_column]
    #         duration = df.loc[i, time_end_column] - df.loc[i, time_start_column]

    #         # Storing the column numbers as a string
    #         group_data.loc[i, f'Case{case_number}_on_cols'] = ', '.join(on_columns)
    #         group_data.loc[i, f'Case{case_number}_off_cols'] = ', '.join(off_columns)
    #         group_data.loc[i, f'Case{case_number}_confidence'] = confidence_level
    #         group_data.loc[i, f'Case{case_number}_duration'] = duration
    #         # group_data.loc[i, f'Case{case_number}_time_start'] = time_start
    #         # group_data.loc[i, f'Case{case_number}_time_end'] = time_end
    # # Add a column to distinguish the group
    # group_data['Group'] = sheet_name
    # group_data['C++'] = df["Q5_1"]
    # group_data['Vul'] = df["Q8_1"]

    # # Append the group's data to the all_groups_data DataFrame
    # all_groups_data = pd.concat([all_groups_data, group_data], ignore_index=True)

# Reset index to represent participant IDs more clearly
# all_groups_data.index.name = 'Participant'
# all_groups_data.reset_index(inplace=True)
# all_groups_data['Participant'] = all_groups_data['Participant'].apply(lambda x: f'Participant {x}')

# Save the all_groups_data DataFrame to a CSV file
# csv_output_path = 'final_output_table.csv'  # Define your desired output file path
# all_groups_data.to_csv(csv_output_path, index=False)

# print(f'The output table has been saved to {csv_output_path}')
