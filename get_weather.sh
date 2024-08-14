#!/bin/bash
source /home/user/miniforge3/etc/profile.d/conda.sh
eval "$(conda shell.bash hook)"
conda activate iccd332
python3 /home/user/proyecto/get_weather.py