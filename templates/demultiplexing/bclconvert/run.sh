#!/bin/bash
# BPM Template: demultiplexing/bclconvert

# Enable strict mode: exit on error, undefined vars, and pipeline failures
set -euo pipefail

# Run bcl-convert
echo "🚀 Running bcl-convert..."
{{ repo_config.environment.tool_paths.bclconvert }} \
  --bcl-input-directory "{{ bcl_path }}" \
  --output-directory out_fastq \
  --sample-sheet samplesheet.csv \
  --no-lane-splitting true \
  --bcl-num-conversion-threads {{ num_threads // 3 }} \
  --bcl-num-compression-threads {{ num_threads // 3 }} \
  --bcl-num-decompression-threads {{ num_threads // 3 }}
# --bcl-sampleproject-subdirectories true \

# Run FASTQC
echo "🔬 Running FASTQC..."
mkdir -p {{ output_dir }}/fastqc
find {{ output_dir }} -maxdepth 2 -name "*.fastq.gz" | parallel -j {{ num_threads }} {{ repo_config.environment.tool_paths.fastqc }} {} -o {{ output_dir }}/fastqc

# Conditionally run fastq_screen
{% if run_fastq_screen %}
echo "🔎 Running fastq_screen..."
mkdir -p {{ output_dir }}/fastq_screen
find {{ output_dir }} -maxdepth 2 -name "*.fastq.gz" | parallel -j {{ num_threads }} {{ repo_config.environment.tool_paths.fastq_screen }} --outdir {{ output_dir }}/fastq_screen {}
{% else %}
echo "⏭️ Skipping fastq_screen..."
{% endif %}

# Run MultiQC
echo "📊 Running MultiQC..."
mkdir -p {{ output_dir }}/multiqc
{{ repo_config.environment.tool_paths.multiqc }} -f {{ output_dir }} -o {{ output_dir }}/multiqc

# Cleanup
echo "🧹 Cleaning up..."
rm -rf {{ output_dir }}/fastqc
[[ -d {{ output_dir }}/fastq_screen ]] && rm -rf {{ output_dir }}/fastq_screen

echo "✅ Done."

bpm update --template demultiplexing:bclconvert --project ./project.yaml
