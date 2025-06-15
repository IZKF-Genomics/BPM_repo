from pathlib import Path
from typing import Any, Dict


def get_template_target_dir(inputs: Dict[str, Any]) -> Path:
    """Locate the template target directory.
    
    Args:
        inputs: Dictionary of input parameters (unused)

    Returns:
        Path to the template target directory
    """
    for key, value in inputs.items():
        print(key, value)
    section, template_name = inputs["template"].split(":")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(Path(inputs["project_dir"]) / section / template_name)
    return Path(inputs["project_dir"]) / section / template_name