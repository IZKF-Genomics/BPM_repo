import os
import glob
import sys


def generate_samplesheet_nfcore_rnaseq(
    fastq_dir,
    samplesheet_file,
    strandedness="unstranded",
    read1_extension="_R1_001.fastq.gz",
    read2_extension="_R2_001.fastq.gz",
    single_end=False,
    sanitise_name=False,
    sanitise_name_delimiter="_",
    sanitise_name_index=1,
    sc=False,
    r16s=False
):
    """
    Generate a samplesheet for nf-core RNA-seq pipeline from FastQ files.
    
    Args:
        fastq_dir (str): Directory containing FastQ files
        samplesheet_file (str): Path to output samplesheet file
        strandedness (str): Library strandedness (unstranded, forward, reverse)
        read1_extension (str): Extension for read 1 files
        read2_extension (str): Extension for read 2 files
        single_end (bool): Whether the data is single-end
        sanitise_name (bool): Whether to sanitize sample names
        sanitise_name_delimiter (str): Delimiter for sanitizing names
        sanitise_name_index (int): Index for sanitizing names
        sc (bool): Whether the data is single-cell
        r16s (bool): Whether the data is 16S rRNA
    """
    def remove_end_slash(path):
        """Remove the ending slash in the given path."""
        if path.endswith("/"):
            path = path.rstrip("/")
        return path

    def sanitize_sample(path, extension):
        """Retrieve sample id from filename"""
        sample = os.path.basename(path).replace(extension, "")
        if sanitise_name:
            sample = sanitise_name_delimiter.join(
                os.path.basename(path).split(sanitise_name_delimiter)[
                    :sanitise_name_index
                ]
            )
        return sample

    def get_fastqs(extension):
        """Get sorted list of FastQ files with given extension"""
        return sorted(
            glob.glob(os.path.join(fastq_dir, f"*{extension}"),
                      recursive=False)
        )

    # Validate strandedness
    if strandedness not in ["unstranded", "forward", "reverse"]:
        strandedness = "unstranded"

    # Remove trailing slash from fastq_dir
    fastq_dir = remove_end_slash(fastq_dir)

    read_dict = {}

    # Get read 1 files
    for read1_file in get_fastqs(read1_extension):
        sample = sanitize_sample(read1_file, read1_extension)
        if sample.startswith("Undetermined"):
            continue
        if sample not in read_dict:
            read_dict[sample] = {"R1": [], "R2": []}
        read_dict[sample]["R1"].append(os.path.join(fastq_dir, read1_file))

    # Get read 2 files
    if not single_end:
        for read2_file in get_fastqs(read2_extension):
            sample = sanitize_sample(read2_file, read2_extension)
            if sample.startswith("Undetermined"):
                continue
            read_dict[sample]["R2"].append(os.path.join(fastq_dir, read2_file))

    # Write to file
    if len(read_dict) > 0:
        out_dir = os.path.dirname(samplesheet_file)
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir)

        with open(samplesheet_file, "w") as file:
            if sc:
                header = ["sample", "fastq_1", "fastq_2"]
            elif r16s:
                header = ["sampleID", "forwardReads", "reverseReads", "run"]
            else:
                header = ["sample", "fastq_1", "fastq_2", "strandedness"]
            file.write(",".join(header) + "\n")
            for sample, reads in sorted(read_dict.items()):
                for idx, read_1 in enumerate(reads["R1"]):
                    read_2 = ""
                    if idx < len(reads["R2"]):
                        read_2 = reads["R2"][idx]
                    if sc:
                        sample_info = ",".join([sample, read_1, read_2])
                    elif r16s:
                        sample_info = ",".join([sample, read_1, read_2, "1"])
                    else:
                        sample_info = ",".join([sample, read_1, read_2,
                                                strandedness])
                    file.write(f"{sample_info}\n")
    else:
        error_str = (
            "\nWARNING: No FastQ files found!\n\n"
        )
        error_str += "Please check the values provided for the:\n"
        error_str += "  - Path to the directory containing the FastQ files\n"
        error_str += "  - '--read1_extension' parameter\n"
        error_str += "  - '--read2_extension' parameter\n"
        print(error_str)
        sys.exit(1)