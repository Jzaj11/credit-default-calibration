from pathlib import Path
import yaml
import random
import numpy as np


def load_config(config_path: Path ):
    """
    Load configuration from a YAML file.
    Args:
        config_path (Path): Path to the configuration file.
    Returns:
        dict:Dictionray with project configuration parameters.
        """
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

def set_seed(seed: int):
    """
    Set the random seed for reproducibility.

    Args:
        seed (int): The seed value to set.
    """
 
    random.seed(seed)
    np.random.seed(seed)

def get_data_path(config:dict, project_root:Path, directory: str):
    """ Return an absolute path to the data directory specified in the configuration.
    
    Args:
        config (dict): Configuration dictionary containing the data directory path.
        project_root (Path): Path to the root of the project.
        directory (str): Key in the configuration dictionary for the desired data directory."""
    relative_path = config["data"][directory]
    return project_root / relative_path