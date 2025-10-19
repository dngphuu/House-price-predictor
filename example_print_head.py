# example_print_head.py
# Simple demonstration of df.head() behavior in a script vs interactive shell
import pandas as pd

def main():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e']
    })

    print("Created DataFrame with shape:", df.shape)

    print("\nCalling df.head() without print() (no visible output expected in a script):")
    df.head()  # This returns a DataFrame but doesn't print anything in a plain script
    print("-> The previous df.head() call produced no output in this script.")

    print("\nNow calling print(df.head()):")
    print(df.head())

    print("\nNote: In interactive environments like Jupyter/IPython, simply writing df.head() shows a table. In a normal python script you must use print() to send output to stdout.")

if __name__ == '__main__':
    main()

