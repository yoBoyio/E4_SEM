import pandas as pd

# Define a function to calculate precision
def calculate_precision(TP, FP):
    return TP / (TP + FP) if (TP + FP) > 0 else 0

# Define the Excel file path
file_path = '1.xlsx'  # Make sure to update this with the correct file path

sheet_names = ['A','B','C','D']
gitHub_ground_truth_table = {
    1:'ELEVATION-PRIVELEDGED-ACCESS',
    2:'',
    3:'MALISCIOUS-CODE-GIHUB',
    4:'DOS-SERVER',
    5:'',
    6:'',
    7:'',
    8:'LEAKED-CONFIG-FILE',
    9:'DOS-REMOTE-REPO',
    10:'STOLEN-AUTH-INFO',
}

k8_ground_truth_table = {
    1:'LEAKED-PRIVELEGE-REMOTE',
    2:'SPOOFING-AUTH-WORKLOAD',
    3:'DOS-WORKERNODE',
    4:'ELEVATION-PRIVELEDGED-ACCESS',
    5:'EXPLOIT-PRIVELEDGED-CONTAINER',
    6:'',
    7:'',
    8:'',
    9:'',
    10:'',
}

# Load the Excel file
xls = pd.ExcelFile(file_path)
results = []

for sheet_name in sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    # group_data = pd.DataFrame()
    for index, row in df.iterrows():
        non_empty_cells = 0
        
        # Check each cell in the row
        for cell in row[:10]:
            
            print(cell)
         