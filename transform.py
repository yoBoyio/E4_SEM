import pandas as pd

def calculate_row_precision(row, table):
    tp = 0 
    fp = 0
    
    # Iterate over each cell in the row
    for cellIndex in range(1,11):
        if pd.notna(row[cellIndex]) and table[cellIndex-1] in str(row[cellIndex]):
           tp += 1
        else:  
            fp += 1
    
    # Calculate precision, avoid division by zero
    precision = tp / (tp + fp) if (tp + fp) > 0 else None  # Undefined if no TP and FP
    return precision

def calculate_row_recall(row, table):
    tp = 0  
    fn = 0      
    for cellIndex in range(1, 11):
            # If the cell content matches the condition, it's a TP
            if pd.notna(row[cellIndex]) and table[cellIndex-1] in str(row[cellIndex]):
                tp += 1
            # If the cell content does not match the condition, but should (according to table), it's an FN
            else:
                fn += 1
    
    # Calculate recall, avoid division by zero
    recall = tp / (tp + fn) if (tp + fn) > 0 else None  # Undefined if no TP and FN
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
        results.append({'Group': sheet_name,'Scenario': 'GitHub', 'Precision Score': precision_score_gh, 'Recall Score': recall_score_gh})
        print('k8 start ================================================================')
        recall_score_k8 = calculate_row_recall(row[11:], k8_ground_truth_table)
        precision_score_k8 = calculate_row_precision(row[11:], k8_ground_truth_table)
        results.append({'Group': sheet_name,  'Scenario': 'K8', 'Precision Score': precision_score_k8, 'Recall Score': recall_score_k8})
        print('k8 end ================================================================')

results_df = pd.DataFrame(results)
output_csv_path = 'metrics_table.csv'
results_df.to_csv(output_csv_path, index=False)          
print(results)