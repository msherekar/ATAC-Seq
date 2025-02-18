import argparse
from .preprocessing import preprocess_data
from termcolor import colored

def main():
    parser = argparse.ArgumentParser(description="ATAC-Seq Data Preprocessing Pipeline")
    parser.add_argument("-i", "--input", type=str, required=True, help="Path to input FASTQ file")
    parser.add_argument("-o", "--output", type=str, required=True, help="Path to output BAM file")

    args = parser.parse_args()

    print(colored(f"🚀 Running preprocessing on {args.input}", "magenta"))
    preprocess_data(args.input, args.output)

if __name__ == "__main__":
    main()
