# local macbook has python2 by default.
# using virtualenv with preinstalled python3, django etc ("myenv")
if [ "$(whoami)" == "kml" ]; then
    source ~/myenv/bin/activate
    echo "hi Kostia"
fi

python manage.py runserver

if [ "$(whoami)" == "kml" ]; then
    deactivate
    printf "\n"
    echo "bye Kostia"
fi