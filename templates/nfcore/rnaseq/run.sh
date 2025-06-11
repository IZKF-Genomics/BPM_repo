#!/bin/bash

# =============================================================================
# nf-core/rnaseq Pipeline Runner
# =============================================================================
# This script runs the nf-core/rnaseq pipeline for RNA-seq analysis.
# It supports various configurations including different genomes and UMI processing.
#
# Usage:
#   ./run.sh
#
# Requirements:
#   - Nextflow
#   - Docker
#   - Samplesheet in CSV format
# =============================================================================

################## GPM samplesheet #####################
# Command to generate samplesheet for RNA-seq analysis
# Options:
#   -st 'reverse': Stranded reverse
#   -sn true: Sample names enabled
#   -si 2: Sample index
# Usage:
# gpm samplesheet-rnaseq -st 'reverse' -sn true -si 2 samplesheet.csv PROJECT_FASTQ_PATH

################## Run nfcore pipeline #################
# Main pipeline execution command
# Parameters:
#   -r 3.17.0: Pipeline version
#   -profile docker: Use Docker for containerization
#   -c nextflow.config: Custom Nextflow configuration
#   --input: Input samplesheet
#   --outdir: Output directory
#   --genome: Reference genome
#   --gencode: Use GENCODE annotation
#   --featurecounts_group_type: Feature counting method

{{ repo_config.environment.tool_paths.nextflow }} run nf-core/rnaseq \
    -r 3.17.0 -profile docker \
    -c nextflow.config \
    --input samplesheet.csv --outdir results \
    --genome GENCODE_GRCh38_v46  \
    --gencode --featurecounts_group_type gene_type
    # --with_umi --umitools_extract_method "regex" --umitools_bc_pattern2 "^(?P<umi_1>.{8})(?P<discard_1>.{6}).*" # Takara Bio SMARTer® Stranded Total RNA-Seq Kit v3	

###### For rerun the pipeline #################################
# To resume a failed or interrupted run:
# Add the -resume flag to the nextflow command
# Example: nextflow run nf-core/rnaseq ... -resume

###### Options for genome: ####################################
# Available genome options:
# - GENCODE_GRCh38_v46: Human genome (GRCh38)
# - GENCODE_GRCh38_v46_ERCC: Human genome with ERCC spike-ins
# - GENCODE_GRCm39_v35: Mouse genome (GRCm39)
# - GENCODE_GRCm39_v35_ERCC: Mouse genome with ERCC spike-ins
#
# Additional options:
# --gencode: Use GENCODE annotation
# --featurecounts_group_type gene_type: Group features by gene type

###### For runs with ERCC spike-ins ############################
# When using ERCC spike-in controls:
# 1. Use appropriate genome (e.g., GENCODE_GRCh38_v46_ERCC)
# 2. Add --skip_biotype_qc to skip biotype quality control
# Example:
# --genome GENCODE_GRCh38_v46_ERCC --skip_biotype_qc