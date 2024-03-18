import pandas as pd

def calculate_row_precision(row, table):
    tp = 0 
    fp = 0
    fn = 0

    for cellIndex in range(1, 10):
        cell_value= row[cellIndex].split('.')[1]
        print(cell_value)
        if cell_value in table.keys() and table[cell_value] is True:
            tp += 1
        elif cell_value in table.keys() and table[cell_value] is False:
                fp += 1
        else:
            # Count as FN if the cell is NaN but the truth table expected a non-empty match
            fn += 1

    # # Calculate precision, avoid division by zero
    precision = tp / (tp + fp) if (tp + fp) > 0 else None  # Undefined if no TP and FP

    
    return precision

def calculate_row_recall_precision(row, table):
    tp = 0  
    fn = 0      
    fp = 0      

    for cellIndex in range(1, 11):
        # cell_value= row[cellIndex].split('.')[1]
        # print(cell_value) 
        if pd.isna(row[cellIndex]) and table[cellIndex-1][1] is False :
            tp += 1
        elif pd.isna(row[cellIndex]) and table[cellIndex-1][1] is True:
                fp += 1
        elif row[cellIndex].split('.')[1] in table[cellIndex-1][0] and table[cellIndex-1][0]:
            tp += 1
        elif row[cellIndex].split('.')[1] not in table[cellIndex-1][0] and table[cellIndex-1][0]:
            # Count as FN if the cell is NaN but the truth table expected a non-empty match
            fn += 1

    recall = tp / (tp + fn) if (tp + fn) > 0 else 0  # Calculate recall
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0  # Undefined if no TP and FP

    return recall, precision

file_path = '1.xlsx' 

sheet_names = ['A','B','C','D']
gitHub_ground_truth_table = [
    ('ELEVATION-PRIVELEDGED-ACCESS', True) ,
    ('DISCLOSE-THIRD-PARTY', False),
    ('MALISCIOUS-CODE-GIHUB', True),
    ('DOS-SERVER', True),
    ('ELEVATION-PRIVELEDGED-REPO', False),
    ('ELEVATION-PRIVELEDGED-CODE', False),
    ('EXPLOIT-HTTP-PROTOCOL', False),
    ('LEAKED-CONFIG-FILE', True),
    ('DOS-REMOTE-REPO', False),
    ('STOLEN-AUTH-INFO', True),
]

k8_ground_truth_table = [
    ('LEAKED-PRIVELEGE-REMOTE', True),
    ('SPOOFING-AUTH-WORKLOAD', True),
    ('DOS-WORKERNODE', True),
    ('ELEVATION-PRIVELEDGED-MALICIOUS-IMG', True),
    ('EXPLOIT-PRIVELEDGED-CONTAINER', True),
    ('PORT-JAMMING-NETWORK-POLICIES', False),
    ('LEAKED-SECRET-DOCKERFILE', False),
    ('CHAIN-ATTACK-MALICIOUS-INPUTS', False),
    ('UNAUTH-CONFIG-TAMPERING', False),
    ('SPOOFING-LAYER-3', False),
]
xls = pd.ExcelFile(file_path)
results = []
counterParticipant = 0
for sheet_name in sheet_names:
    df = pd.read_excel(xls,skiprows=1, sheet_name=sheet_name,)
    for index, row in df.iterrows():
        recall_score_gh, precision_score_gh = calculate_row_recall_precision(row, gitHub_ground_truth_table)
        counterParticipant += 1
        results.append({'SID': counterParticipant , 'Group': sheet_name,'Scenario': 'GitHub', 'Precision Score': precision_score_gh, 
                        'Recall Score': recall_score_gh, 'GitHub Familarity': row[23],'K8 Familarity': row[24], 'Understanding': row[22]})
        recall_score_k8, precision_score_k8 = calculate_row_recall_precision(row[11:], k8_ground_truth_table)
        counterParticipant += 1
        results.append({'SID': counterParticipant, 'Group': sheet_name,  'Scenario': 'K8', 'Precision Score': precision_score_k8,
                         'Recall Score': recall_score_k8, 'GitHub Familarity': row[23],'K8 Familarity': row[24], 'Understanding': row[22]})

results_df = pd.DataFrame(results)
output_csv_path = 'metrics_table.csv'
results_df.to_csv(output_csv_path, index=False)          