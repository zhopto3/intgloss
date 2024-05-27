import os
import torch
import shutil
import argparse
import pandas as pd

from data import GlossingDataset
from pytorch_lightning import Trainer
from ctc_model import CTCGlossingModel
from morpheme_model import MorphemeGlossingModel
from pytorch_lightning import loggers as pl_loggers
from pytorch_lightning.callbacks import EarlyStopping
from pytorch_lightning.callbacks import ModelCheckpoint

language_code_mapping = {
    "Arapaho": "arp",
    "Gitksan": "git",
    "Lezgi": "lez",
    "Natugu": "ntu",
    "Nyangbo": "nyb",
    "Tsez": "ddo",
    "Uspanteko": "usp",
}

if __name__ == "__main__":
    # Set torch matmul precision
    torch.set_float32_matmul_precision("high")

    # Make experiment name
    #name = f"glossing_{args.model}_{args.language}_{args.track}"

    # Make experiment directory

    # Load data
    language = "Gitksan"
    track = 1
    language_code = language_code_mapping[language]

    train_file = f"./data/{language}/{language_code}-train-track{track}-uncovered"
    validation_file = f"./data/{language}/{language_code}-dev-track{track}-uncovered"
    test_file = f"./data/{language}/{language_code}-dev-track{track}-covered"

    dm = GlossingDataset(
        train_file=train_file,
        validation_file=validation_file,
        test_file=test_file,
        batch_size=256,
    )

    dm.prepare_data()
    dm.setup(stage="fit")

    train = dm.train_dataloader()

    print(next(iter(train)))