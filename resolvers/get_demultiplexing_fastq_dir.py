from pathlib import Path
from typing import Any, Dict, List
import os
import glob


def get_demultiplexing_fastq_dir(inputs: Dict[str, Any]) -> Path:
    """Locate the demultiplexing fastq directory.
    
    Args:
        inputs: Dictionary of input parameters (unused)
        
    Returns:
        Path to the demultiplexing fastq directory
    """
    return inputs["fastq_dir"]