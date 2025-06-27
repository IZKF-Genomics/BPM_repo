from pathlib import Path
from typing import Any, Dict


def get_template_target_dir(inputs: Dict[str, Any]) -> Path:
    """Locate the template target directory.
    
    Args:
        inputs: Dictionary of input parameters (unused)

    Returns:
        Path to the template target directory
    """
    section, template_name = inputs["cmd_params.template"].split(":")
    target_dir = Path(inputs["project.info.project_dir"]) / section / template_name
    return target_dir