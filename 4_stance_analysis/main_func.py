import numpy as np
import pandas as pd
import pred as pred

SIZE_SSM = 47346
SIZE_LGBT = 32788
SIZE_GENDER = 2564
headlines_fn = "headlines_final/headlines_final.csv"
temp_headlines_fn = "headlines_final/headlines.csv"
predictions_fn = "headlines_final/final_predictions.csv"
switcher ={
        "same-sex marriage": "same-sex marriage",
        "lgbt": "lgbt",
        "gender_identity": "gender_identity"
    }

df_headlines = pd.read_csv(headlines_fn)

topic= "same-sex marriage"

if topic == "same-sex marriage":
    quotes = "data_ssm.csv"
    size_data = SIZE_SSM
elif topic == "lgbt":
    quotes = "final_test/data_lgbtq.csv"
    size_data = SIZE_LGBT
else:
    quotes = "final_test/data_gender.csv"
    size_data = SIZE_GENDER

df_model_output = pd.read_csv("model_output.csv")
df_output = pd.DataFrame(index=range(32788), columns=['stance'])
print("starting the outter for")
print (len(df_headlines))
h_dataframe = pd.DataFrame(index=range(32788))
#for num, headline in df_headlines.iterrows():
h_dataframe['Headline'] = df_headlines['headline'][15]
print(df_headlines['headline'][15])
h_dataframe.index.names = ["Body ID"]
h_dataframe.to_csv(temp_headlines_fn)
pred.main(temp_headlines_fn, quotes, predictions_fn)
df_pred = pd.read_csv(predictions_fn)
for num, predi in df_pred.iterrows():
    if predi['Stance'] == "agree":
        df_model_output['agree'][num] += 1
    elif predi['Stance'] == "disagree":
        df_model_output['disagree'][num] += 1
    elif predi['Stance'] == "discuss":
        df_model_output['discuss'][num] += 1 
    elif predi['Stance'] == "unrelated":
        df_model_output['unrelated'][num] += 1 
print("ended the first for")  
df_model_output.to_csv(r'model_output.csv')
