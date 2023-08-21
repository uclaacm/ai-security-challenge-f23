import torch
from torch.utils import data

from torchvision import datasets, transforms

class StartingDataset(data.Dataset):
    """
    Dataset that contains 100000 3x224x224 black images (all zeros).
    """

    def __init__(self):
        self.dataset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transforms.ToTensor())

    def __getitem__(self, index):
        inputs = torch.zeros([3, 224, 224])
        label = 0

        return inputs, label

    def __len__(self):
        return 10000
