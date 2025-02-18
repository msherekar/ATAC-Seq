import subprocess
from termcolor import colored

def run_samtools_index(bam_file):
    """
    Indexes the sorted BAM file.
    """
    print(colored(f"🔹 Indexing {bam_file}...", "yellow"))

    command = [
        "samtools", "index", bam_file
    ]

    try:
        subprocess.run(command, check=True)
        print(colored(f"✅ Indexing completed: {bam_file}.bai", "green"))
    except FileNotFoundError:
        print(colored("❌ Samtools is not installed!", "red"))
    except subprocess.CalledProcessError as e:
        print(colored(f"❌ Error indexing BAM file: {e}", "red"))

if __name__ == "__main__":
    run_samtools_index("example_sorted.bam")