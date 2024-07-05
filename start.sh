# !/bin/bash

gnome-terminal -- bash -c "source /home/jmcada/Documents/UNAL/6s/software/historia_clinica/venv/bin/activate; python3 /home/jmcada/Documents/UNAL/6s/software/historia_clinica/backend/manage.py runserver; bash"
gnome-terminal -- bash -c "cd /home/jmcada/Documents/UNAL/6s/software/historia_clinica/frontend/; npm run dev; bash"
