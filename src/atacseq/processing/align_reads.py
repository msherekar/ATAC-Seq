import subprocess
from termcolor import colored
from .. import config

def run_bowtie2(input_fastq, output_bam):
    """
    Aligns ATAC-Seq reads to the reference genome using Bowtie2.
    """
    print(colored(f"🔹 Aligning {input_fastq} using Bowtie2...", "yellow"))

    command = [
        "bowtie2",
        "-x", config.GENOME_INDEX,  # Genome index path
        "-U", input_fastq,
        "-S", output_bam.replace(".bam", ".sam"),
        "--very-sensitive"
    ]

    try:
        subprocess.run(command, check=True)
        print(colored(f"✅ Alignment completed: {output_bam}", "green"))
    except FileNotFoundError:
        print(colored("❌ Bowtie2 is not installed! Install it using `conda install -c bioconda bowtie2`", "red"))
    except subprocess.CalledProcessError as e:
        print(colored(f"❌ Error running Bowtie2: {e}", "red"))

if __name__ == "__main__":
    run_bowtie2("input.fastq", "output.bam")
