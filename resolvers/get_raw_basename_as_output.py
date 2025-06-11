from pathlib import Path
from typing import Any, Dict

def get_raw_basename_as_output(inputs: Dict[str, Any]) -> Path:
    """Get the raw basename as output."""
    # if inputs["output_dir"] is None:
    cwd = Path.cwd()
    bcl_path = inputs["bcl_path"].name
    return cwd / bcl_path
    # else:
    #     return inputs["output_dir"]
