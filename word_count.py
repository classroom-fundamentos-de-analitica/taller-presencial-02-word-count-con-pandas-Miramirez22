"""Taller evaluable"""

import glob
import pandas as pd
import string


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    filenames = glob.glob(input_directory + "/*.*")
    sequence = []

    for filename in filenames:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                sequence.append((filename, line.strip()))
    
    df = pd.DataFrame(sequence, columns=["filename", "line"])
    return df

def clean_text(dataframe):
    """Text cleaning"""
    dataframe["line"] = dataframe["line"].str.lower().str.translate(str.maketrans("", "", string.punctuation))
    return dataframe

def count_words(dataframe):
    """Word count"""
    dataframe = dataframe.line.str.split(expand=True).stack().value_counts().reset_index()
    dataframe.columns = ["word", "count"]
    return dataframe

def save_output(dataframe, output_filename):
    """Save output to a file."""
    dataframe.to_csv(output_filename, sep=";", index=False)

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    
    df = load_input(input_directory)
    df = clean_text(df)
    df = count_words(df)
    save_output(df, output_filename)

if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )



