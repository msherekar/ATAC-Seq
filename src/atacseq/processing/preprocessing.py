

from .cutadapt_trim import run_cutadapt
from .align_reads import run_bowtie2
from .samtools_sort import run_samtools_sort
from .samtools_index import run_samtools_index
from termcolor import colored

def preprocess_data(input_fastq, output_bam):
    """
    Runs the full preprocessing pipeline.
    """
    print(colored("🚀 Starting ATAC-Seq Preprocessing...", "magenta"))

    trimmed_fastq = input_fastq.replace(".fastq.gz", "_trimmed.fastq.gz")
    sam_file = output_bam.replace(".bam", ".sam")

    # Step 1: Trim adapters
    run_cutadapt(input_fastq, trimmed_fastq)

    # Step 2: Align reads to the genome
    run_bowtie2(trimmed_fastq, output_bam)

    # Step 3: Sort BAM file
    run_samtools_sort(sam_file, output_bam)

    # Step 4: Index BAM file
    run_samtools_index(output_bam)

    print(colored("✅ ATAC-Seq Preprocessing Complete!", "green"))

if __name__ == "__main__":
    input_fastq = "/Users/mukulsherekar/pythonProject/atacsec-project/data/ENCFF890OIZ.fastq.gz"
    output_bam = "/Users/mukulsherekar/pythonProject/atacsec-project/output/ENCFF890OIZ.bam"
    preprocess_data(input_fastq, output_bam)
    # later make sure the output name is automatically setup by input file