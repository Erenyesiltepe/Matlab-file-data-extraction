from scipy.io import loadmat
import pandas as pd

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
    
    import pdb; pdb.set_trace()
    
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
        'Rating': rating
    })
    return df    

exp_data = load_recall_data("experimentRecall_data.mat")
print(exp_data)

# exp_recall_data = loadmat('experimentRecall_data.mat')['recalldata']
# exp_recall_data = parse(exp_recall_data) 

# exp_data.to_excel('experimentData.xlsx', index=False)
# exp_recall_data.to_excel('experimentDataRecall.xlsx', index=False)
