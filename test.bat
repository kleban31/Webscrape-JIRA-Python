
echo off

set "pathf=C:\Users\Michael Kleban\Documents\PY4e\JIRAScrape-env\Scripts\MainScripts\jiratable.sqlite"
set path=C:\Users\Michael Kleban\Documents\PY4e\JIRAScrape-env\Scripts\MainScripts

echo %path%
for %%G in (*.sqlite*) do set jfs=%%~zG



if %jfs% gtr 16000 (
echo too much
echo go away
) else (
echo howdy doody
echo you are on queue
)
