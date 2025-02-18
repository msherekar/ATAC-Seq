import subprocess
from termcolor import colored

def run_cutadapt(input_fastq, output_fastq):
    """
    Trims adapters from raw ATAC-Seq reads using Cutadapt.
    """
    print(colored(f"🔹 Running Cutadapt on {input_fastq}...", "yellow"))

    command = [
        "cutadapt",
        "-a", "AGATCGGAAGAGC",  # Replace with correct adapter sequence
        "-q", "20",  # Quality trimming threshold
        "-o", output_fastq,
        input_fastq
    ]

    try:
        subprocess.run(command, check=True)
        print(colored(f"✅ Cutadapt completed: {output_fastq}", "green"))
    except FileNotFoundError:
        print(colored("❌ Cutadapt is not installed! Install it using `conda install -c bioconda cutadapt`", "red"))
    except subprocess.CalledProcessError as e:
        print(colored(f"❌ Error running Cutadapt: {e}", "red"))

if __name__ == "__main__":
    input_fastq = "/Users/mukulsherekar/pythonProject/atacsec-project/data/ENCFF890OIZ.fastq.gz"
    output_fastq = "/Users/mukulsherekar/pythonProject/atacsec-project/output/ENCFF890OIZ_output"
    run_cutadapt(input_fastq, output_fastq)

# TODO: Add arg variable for adapter sequence