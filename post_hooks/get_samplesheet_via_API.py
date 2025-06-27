from typing import Dict, Any
from bpm.utils.ui.console import BPMConsole

console = BPMConsole()

def get_samplesheet_via_API(inputs: Dict[str, Any]) -> None:
    """Get the samplesheet via API."""
    console.dict(inputs)
    # Get the samplesheet via API
    # Save the samplesheet to the project
    # Update the project with the samplesheet
    # Save the project
    # Return the samplesheet
    return