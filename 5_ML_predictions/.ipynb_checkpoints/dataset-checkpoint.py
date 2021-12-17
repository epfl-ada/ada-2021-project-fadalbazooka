import torch
from torch.utils.data import Dataset
import pandas as pd
from transformers import AutoTokenizer, AutoModel
import numpy as np

MODEL = "cardiffnlp/twitter-roberta-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModel.from_pretrained(MODEL)


def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)


def get_embedding(text):
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    features = model(**encoded_input)
    features = features[0].detach().cpu().numpy()
    features_mean = np.mean(features[0], axis=0)
    return features_mean


class QuoteDataset(Dataset):
    """
    PyTorch Dataset which loads quotes
    """

    def __init__(self, path="./filtered.json"):
        """
        Initialize dataset parameters
        :param path: path to json dataset
        """
        self.data = pd.read_json(path)
        nationalities = np.unique([i for i in np.hstack(self.data.nationality.dropna().to_numpy()) if i is not None])
        self.dict_nationalities = {elem: idx / len(nationalities) for idx, elem in enumerate(nationalities)}

    def __len__(self):
        return self.data.shape[0]

    def __getitem__(self, item):
        quote = torch.Tensor(get_embedding(self.data.Quote.iloc[item]).reshape(1, -1))
        nationality = self.dict_nationalities[self.data.nationality.iloc[item][0]]
        return quote, nationality

