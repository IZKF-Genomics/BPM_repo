from pathlib import Path
from typing import Any, Dict

# The inputs parameter is the collection of all parameters from the project.yaml, repo's config files, and command line parameters. All parameters are stored in a dictionary in the following structure:
# {"project":
# 
def get_cwd(inputs: Dict[str, Any]) -> Path:
    """Get the current working directory."""
    return Path.cwd()
