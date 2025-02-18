import subprocess
import os
from termcolor import colored

def run_samtools_sort(input_sam, output_bam):
    """
    Converts SAM to BAM and sorts the reads.
    """
    print(colored(f"🔹 Sorting BAM file {output_bam}...", "yellow"))

    command = [
        "samtools", "sort",
        "-o", output_bam,
        input_sam
    ]

    try:
        subprocess.run(command, check=True)
        print(colored(f"✅ Sorting completed: {output_bam}", "green"))
        
        # Remove intermediate SAM file
        os.remove(input_sam)

    except FileNotFoundError:
        print(colored("❌ Samtools is not installed! Install it using `conda install -c bioconda samtools`", "red"))
    except subprocess.CalledProcessError as e:
        print(colored(f"❌ Error sorting BAM file: {e}", "red"))

if __name__ == "__main__":
    
    run_samtools_sort("example.sam", "example_sorted.bam")