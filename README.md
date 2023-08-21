# adversarial-ai-attack-defense-template
Template repository for the adversarial AI attack-defense project run by ACM Cyber x ACM Cyber. Fall 2023.

## Setup

1. Create a new conda environment.

2. Install PyTorch.

3. As you work on the project, you will end up installing many more packages.

## Running the Skeleton Code

### Running the Code Locally

After activating your conda environment, run the following command:

```
python main.py
```

### Running the Code on Google Colab

[This notebook]() will walk you through setting the skeleton code up on Google Colab.

**Note:** Google Colab may terminate your session after a few hours, so it may be a better idea to run your code on Kaggle (see below).

### Running the Code on Kaggle

[This notebook](https://www.kaggle.com/franktzheng/acm-ai-projects-kaggle-skeleton) will walk you through setting the skeleton code up on Kaggle.

1. Navigate to the [code tab of the Kaggle competition](https://www.kaggle.com/c/cassava-leaf-disease-classification/code). Click on the "New Notebook" button to create a new notebook. The dataset should be automatically loaded in the `/kaggle/input` folder.

2. To use the GPU, click the three dots in the top-right corner and select Accelerator > GPU.

3. To access your code, run the following command (replacing the URL):

   ```
   !git clone "https://github.com/uclaacmai/projects-skeleton-code"
   ```

   This should clone your repository into the `/kaggle/working` folder.

4. Change directories into your repository by running the command:

   ```
   cd <name of your repository>
   ```

5. You should now be able to import your code normally. For instance, the following code will import the starting code:

   ```python
   import constants
   from datasets.StartingDataset import StartingDataset
   from networks.StartingNetwork import StartingNetwork
   from train_functions.starting_train import starting_train
   ```

6. If you want your code to run without keeping the tab open, you can click on "Save version" and commit your code. Make sure to save any outputs (e.g. log files) to the `/kaggle/working`, and you should be able to access them in the future.

**IMPORTANT:** If you want to pull new changes in the Kaggle notebook, first run `!git pull`, and then RESTART your notebook (Run > Restart & clear all outputs).

## Downloading the Dataset From Kaggle

### Method 1: Downloading from kaggle.com

1. Go to [kaggle.com](kaggle.com) and create an account.

2. Join either the [Cassava leaf](https://www.kaggle.com/c/cassava-leaf-disease-classification) or [Humpback whale](https://www.kaggle.com/c/humpback-whale-identification) competition.

3. In the data tab, you should be able to download the data as a zip file.

### Method 2: Downloading from the Kaggle API

1. Install the Kaggle API:

   ```
   pip install kaggle
   ```

   If you're on Mac or Linux, you may have to run:

   ```
   pip install --user kaggle
   ```

2. Copy the `kaggle.json` file to the location `~/.kaggle/kaggle.json` (or `C:\Users\<Windows-username>\.kaggle\kaggle.json` if you are on Windows).

3. Download the zipped dataset.

   ```
   # Use humpback-whale-identification for 🐋 dataset
   kaggle competitions download -c cassava-leaf-disease-classification
   ```
