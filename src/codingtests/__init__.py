import pandas as pd
import numpy as np
from datasets import load_dataset

class Question1:
    df = load_dataset("DJ-Research/codingtest", "question1", split="df").to_pandas()    
    other_df = load_dataset("DJ-Research/codingtest", "question1", split="other_df").to_pandas()

    @staticmethod
    def random_numbers(x):
        if not isinstance(x, int):
            raise ValueError("Input must be an integer.")
        if x <= 5:
            raise ValueError("Input must be a positive integer greater than 5")
        return np.random.randint(-x, x+1)
    
    @staticmethod
    def other_random_numbers(x):
        if not isinstance(x, int):
            raise ValueError("Input must be an integer.")
        if x <= 10:
            raise ValueError("Input must be a positive integer greater than 10")
        return np.random.randint(x)
    
class Question2:
    df = load_dataset("DJ-Research/codingtest", "question2", split="df").to_pandas()
    inference_df = df.loc[:5]
    max_new_tokens = 5
    





