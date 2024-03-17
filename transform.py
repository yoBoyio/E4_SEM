import pandas as pd

def calculate_row_precision(row, table):
    tp = 0 
    fp = 0
    
    # Iterate over each cell in the row
    for cellIndex in range(1,11):
        cell_is_nan = pd.isna(row[cellIndex])
        truth_is_empty = table[cellIndex-1] == ''
        
        # Check if both the cell is NaN and the corresponding truth table entry is an empty string
        if cell_is_nan and truth_is_empty:
            tp += 1  # Count as true positive
        elif not cell_is_nan and pd.notna(row[cellIndex]) and table[cellIndex-1] in str(row[cellIndex]):
            tp += 1  # Standard condition for counting true positives
        else:
            fp += 1  # If none of t
    #     if pd.notna(row[cellIndex]) and table[cellIndex-1] in str(row[cellIndex]):
    #        tp += 1
    #     else:  
    #         fp += 1
    
    # # Calculate precision, avoid division by zero
    precision = tp / (tp + fp) if (tp + fp) > 0 else None  # Undefined if no TP and FP

    
    return precision

def calculate_row_recall(row, table):
    tp = 0  
    fn = 0      
    for cellIndex in range(1, 11):
        cell = row[cellIndex]
        truth = table[cellIndex - 1]

        cell_is_nan = pd.isna(cell)
        truth_is_empty = truth == ''
        
        # Count as TP if both the cell is NaN and the truth table entry is empty string
        # or if the cell matches the condition in the truth table (not considering empty matches here)
        if (cell_is_nan and truth_is_empty) or (not cell_is_nan and truth in str(cell)):
            tp += 1
        elif not cell_is_nan and truth not in str(cell):
            # Count as FN if the cell does not match the non-empty condition it should according to the truth table
            # This assumes the truth table can have non-empty values that we are looking to match
            if not truth_is_empty:  # Only count as FN if the truth table expected something other than empty
                fn += 1
        elif cell_is_nan and not truth_is_empty:
            # Count as FN if the cell is NaN but the truth table expected a non-empty match
            fn += 1

    recall = tp / (tp + fn) if (tp + fn) > 0 else None  # Calculate recall
    return recall

file_path = '1.xlsx' 

sheet_names = ['A','B','C','D']
gitHub_ground_truth_table = [
    'ELEVATION-PRIVELEDGED-ACCESS',
    '',
    'MALISCIOUS-CODE-GIHUB',
    'DOS-SERVER',
    '',
    '',
    '',
    'LEAKED-CONFIG-FILE',
    'DOS-REMOTE-REPO',
    'STOLEN-AUTH-INFO',
]

k8_ground_truth_table = [
    'LEAKED-PRIVELEGE-REMOTE',
    'SPOOFING-AUTH-WORKLOAD',
    'DOS-WORKERNODE',
    'ELEVATION-PRIVELEDGED-ACCESS',
    'EXPLOIT-PRIVELEDGED-CONTAINER',
    '',
    '',
    '',
    '',
    '',
]

xls = pd.ExcelFile(file_path)
results = []

for sheet_name in sheet_names:
    df = pd.read_excel(xls,skiprows=1, sheet_name=sheet_name,)
    for index, row in df.iterrows():
        precision_score_gh = calculate_row_precision(row, gitHub_ground_truth_table)
        recall_score_gh = calculate_row_recall(row, gitHub_ground_truth_table)
        results.append({'SID': index + 1, 'Group': sheet_name,'Scenario': 'GitHub', 'Precision Score': precision_score_gh, 
                        'Recall Score': recall_score_gh, 'GitHub Familarity': row[23],'K8 Familarity': row[24], 'Understanding': row[22]})
        print('k8 start ================================================================')
        recall_score_k8 = calculate_row_recall(row[11:], k8_ground_truth_table)
        precision_score_k8 = calculate_row_precision(row[11:], k8_ground_truth_table)
        results.append({'SID': index + 1, 'Group': sheet_name,  'Scenario': 'K8', 'Precision Score': precision_score_k8,
                         'Recall Score': recall_score_k8, 'GitHub Familarity': row[23],'K8 Familarity': row[24], 'Understanding': row[22]})
        print('k8 end ================================================================')

results_df = pd.DataFrame(results)
output_csv_path = 'metrics_table.csv'
results_df.to_csv(output_csv_path, index=False)          
print(results)