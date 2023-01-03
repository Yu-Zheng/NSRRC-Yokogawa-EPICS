python3 /home/ert3/EPICS_DB/Gen_PV_List.py

screen -dmS SoftIoc
screen -x -S SoftIoc -p 0 -X stuff "softIoc -d /home/ert3/EPICS_DB/FE_EPICS_List_Run.db"
screen -x -S SoftIoc -p 0 -X stuff '\n'
