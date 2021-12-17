import numpy as np

from dataset import QuoteDataset
from model import ClassificationText
from torch.utils.data import DataLoader, SubsetRandomSampler
import torch
import pickle


class TrainModel(object):
    """
    Overall model training
    """

    def __init__(self):
        # hyper parameters
        self.num_epochs = 100  # number of epochs to train
        self.batch_size = 16
        self.train_ratio = 0.8  # part of train data in a full dataset
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  # gpu or cpu
        self.alpha, self.beta1, self.beta2 = 0.0001, 0.9, 0.999  # Adam parameters

        # Initialisation
        self.Model = ClassificationText()  # neural network
        self.Criterion = torch.nn.MSELoss()  # loss function
        self.Optimizer = torch.optim.Adam(self.Model.parameters(), lr=self.alpha, betas=(self.beta1, self.beta2))

        # Tracking losses
        self.train_loss = []  # [total loss] for train
        self.val_loss = []  # [total loss] for validation

    def load_data(self):
        """
        Load initial data to dataloader
        :return:
        """
        dataset = QuoteDataset()
        train_sampler = SubsetRandomSampler(np.arange(int(dataset.__len__() * self.train_ratio)))
        val_sampler = SubsetRandomSampler(np.arange(int(dataset.__len__() * (1 - self.train_ratio)) +
                                                    int(dataset.__len__() * self.train_ratio)))
        self.TrainLoader = DataLoader(dataset, batch_size=self.batch_size, sampler=train_sampler)  # create train loader
        self.ValLoader = DataLoader(dataset, batch_size=self.batch_size, sampler=val_sampler)  # create val loader

    def train_epoch(self):
        """
        Model training for current epoch with training dataset
        :return:
        """
        self.Model.train()
        for (quote, label) in self.TrainLoader:  # run 1 batch
            quote, label = quote.to(self.device), label.to(self.device)  # convert to GPU
            with torch.set_grad_enabled(True):
                self.Optimizer.zero_grad()
                output = self.Model(quote)  # get predictions
                all_loss = self.Criterion(output, label.float())  # get loss
                print("Train loss:", all_loss)
                self.train_loss.append(all_loss)  # accumulate losses
                all_loss.backward()  # backward loss for model fitting
                self.Optimizer.step()  # update optimizer

    def validation_epoch(self):
        """
        Test model on a current epoch with validation data
        :return:
        """
        self.Model.eval()
        for (quote, label) in enumerate(self.ValLoader):  # run 1 batch
            quote, label = quote.to(self.device), label.to(self.device)  # convert to GPU
            with torch.set_grad_enabled(False):
                output = self.Model(quote)  # get predictions
                all_loss = self.Criterion(output, label)  # get loss
                print("Validation loss:", all_loss)
                self.val_loss.append(all_loss)  # accumulate losses

    def train_full(self):
        """
        Run training for all epochs and save weights
        :return:
        """
        self.load_data()  # load data to DataLoaders
        print("*" * 60, "Start training", "*" * 60)
        for epoch in range(self.num_epochs):  # run epoch
            # for every epoch: train -> validation
            self.train_epoch()
            self.validation_epoch(epoch)
            print(f"Epoch {epoch} / {self.num_epochs}: Train loss {self.train_loss[-1]}, "
                  f"Validation loss: {self.val_loss[-1]}")

        # save losses
        with open('train_loss', 'wb') as fp:
            pickle.dump(self.train_loss, fp)
        with open('val_loss', 'wb') as fp:
            pickle.dump(self.val_loss, fp)


if __name__ == '__main__':
    model = TrainModel()
    model.train_full()
