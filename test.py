from scipy.io import loadmat
import pandas as pd
import os

folder_name = 'participants'

def load_data(data_path):
    exp_data = loadmat(data_path)
    data = exp_data['data'][0]
    
    categories = [str(entry[0][0]) for entry in data]
    biomotion_names = [str(entry[1][0]) for entry in data]
    responses = [int(entry[2][0][0]) for entry in data]
    
    df = pd.DataFrame({
        'Category': categories,
        'BiomotionName': biomotion_names,
        'Response': responses
    })
    return df

def load_recall_data(data_path):
    exp_data = loadmat(data_path)
    data = exp_data['recalldata'][0]
    
    categories = [str(entry[0][0]) for entry in data]
    biomotion_names = [str(entry[1][0]) for entry in data]
    responses = [str(entry[2][0]) for entry in data]
    time = [float(entry[3][0][0]) for entry in data]
    rating = [int(entry[4][0][0]) for entry in data]
    
    df = pd.DataFrame({
        'Category': categories,
        'BiomotionName': biomotion_names,
        'Response': responses,
        'Time': time,
        'Rating': rating,
        'SeenPoint': [None for _ in data],
        'NotSeenPoint': [None for _ in data],
    })
    return df    

def runForSubject(directory):
    files = os.listdir(directory)

    recall_data_file = None
    data_file = None

    for file in files:
        if file.startswith('experimentRecall_data'):
            recall_data_file = file
        elif file.startswith('experimentData'):
            data_file = file

    subject = '_'.join(data_file.split('_')[1:])
    
    exp_recall_data = load_recall_data(os.path.join(directory, recall_data_file))
    exp_data = load_data(os.path.join(directory, data_file))
    
    sum_seen = 0   
    sum_not_seen = 0

    for index, row in exp_recall_data.iterrows():
        matching_rows = exp_data[exp_data['BiomotionName'] == row['BiomotionName']]
        if matching_rows.empty:
            if row['Response'] == 'x':
                exp_recall_data.at[index, 'NotSeenPoint'] = 0
            else:
                exp_recall_data.at[index, 'NotSeenPoint'] = 1
                sum_not_seen += 1
        else:
            if row['Response'] == 'x':
                exp_recall_data.at[index, 'SeenPoint'] = 1
                sum_seen += 1
            else:
                exp_recall_data.at[index, 'SeenPoint'] = 0
                
        
    # Add two separate rows at the end
    new_row_1 = {
        'Category': 'Total',
        'SeenPoint': sum_seen,
        'NotSeenPoint': sum_not_seen
    }
    new_row_2 = {
        'Category': 'Percentage',
        'SeenPoint': sum_seen / 35,
        'NotSeenPoint': sum_not_seen / 14
    }
    exp_recall_data = pd.concat([exp_recall_data, pd.DataFrame([new_row_1])], ignore_index=True)
    exp_recall_data = pd.concat([exp_recall_data, pd.DataFrame([new_row_2])], ignore_index=True)


    exp_recall_data.to_excel(os.path.join(directory, f'ResultExperimentData-{subject}.xlsx'), index=False)


directory = os.getcwd()+'\\'+folder_name
for root, dirs, files in os.walk(directory):
    for dir_name in dirs:
        runForSubject(os.path.join(root, dir_name))
    break  # Only consider the top-level directories

