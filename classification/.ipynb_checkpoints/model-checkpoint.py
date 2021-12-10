from torch import nn
import torch
from torch.autograd import Variable


class ClassificationText(nn.Module):

    def __init__(self, batch_size=16, output_size=1, hidden_size=256):
        super(ClassificationText, self).__init__()

        self.batch_size = batch_size
        self.output_size = output_size
        self.hidden_size = hidden_size
        self.embedding_length = 768

        self.lstm = nn.LSTM(self.embedding_length, hidden_size)
        self.label = nn.Linear(hidden_size, output_size)

    def forward(self, text_emb):
        input = text_emb.permute(1, 0, 2)
        batch_size = text_emb.shape[0]
        h_0 = torch.zeros(1, batch_size, self.hidden_size)
        c_0 = torch.zeros(1, batch_size, self.hidden_size)

        output, (final_hidden_state, final_cell_state) = self.lstm(input, (h_0, c_0))
        final_output = self.label(final_hidden_state[-1])
        return final_output.squeeze(1)
