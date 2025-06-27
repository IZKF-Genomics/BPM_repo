from typing import Dict, Any
from bpm.utils.ui.console import BPMConsole

console = BPMConsole()

def construct_samplesheet_nfcore_rnaseq(inputs: Dict[str, Any]) -> None:
    """Construct the samplesheet for the nfcore rnaseq pipeline.
    
    Args:
        inputs: Dictionary of input parameters
    """
    console.dict(inputs)
    # Get the samplesheet from demultiplexing
    demultiplexing_samplesheet = inputs["demultiplexing.samplesheet"]