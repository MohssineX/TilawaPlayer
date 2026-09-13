#!/bin/bash

# mimi is a nice cat 

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# setup.sh
 
if ! command -v pip &> /dev/null; then
    echo "pip is not installed. Please install pip first."
    exit 1
fi
 
pip install -r requirements.txt
# pip install -r requirements.txt --break-system-packages
 
if [ $? -ne 0 ]; then
    exit 1
fi

echo "#!/bin/bash

python3 src/main.py" > run.sh

python3 src/main.py
