from typing import Dict, Any
from bpm.utils.ui.console import BPMConsole
from pathlib import Path
console = BPMConsole()

def get_cmd_output(inputs: Dict[str, Any]) -> Path:
    """Get the output directory from the command parameters."""
    return inputs["cmd_params.output"]