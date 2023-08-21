import os
import argparse

import torch

import constants
from data.dataset import StartingDataset
from networks.network import StartingNetwork
from utils.train import starting_train

"""
TODO:
- implement argparse to get command line arguments
- integrate device to allow for GPU training
- set up attack-defense evaluation and pipeline
"""

def main():
    # Get command line arguments
    hyperparameters = {"epochs": constants.EPOCHS, "batch_size": constants.BATCH_SIZE}

    # TODO: Initialize device
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    print("Epochs:", constants.EPOCHS)
    print("Batch size:", constants.BATCH_SIZE)

    # Initalize dataset and model. Then train the model!
    train_dataset = StartingDataset()
    val_dataset = StartingDataset()
    model = StartingNetwork()
    starting_train(
        train_dataset=train_dataset,
        val_dataset=val_dataset,
        model=model,
        hyperparameters=hyperparameters,
        n_eval=constants.N_EVAL,
    )

if __name__ == "__main__":
    main()
