import os
from pathlib import Path

list_of_file=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingetion.py",
    "src/components/data_tranceformation.py",
    "src/components/model_tariner.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/utils/__init__.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_file:
    filepath=Path(filepath)
    file_dir, file_name=os.path.split(filepath)
    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath, "w") as f:
            pass

