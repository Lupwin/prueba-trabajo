@echo off
echo Activating virtual environment...
call provenv\Scripts\activate

echo Starting Gunicorn...
provenv\Scripts\gunicorn proyecto.wsgi:application --bind 0.0.0.0:%PORT%



echo Deactivating virtual environment...
deactivate