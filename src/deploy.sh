#!/bin/bash

echo "Enter a commit for the push: "
read COMMIT

cd core
mv settings.py basesettings.py
mv cloudsettings.py settings.py

cd ../../
git add .
<<<<<<< HEAD
git commit -m "$COMMIT"
git push --set-upstream origin main
=======
git commit -m "Done for the first version!"
git push --set-upstream origin version_1.1
>>>>>>> 8cef9d5193b53023a4dafd99fed4714ec4bb34ab

cd src/core/
mv settings.py cloudsettings.py
mv basesettings.py settings.py
cd ..
clear