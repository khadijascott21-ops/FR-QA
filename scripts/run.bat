@echo off
rem Launches the Currency Converter (distribution zip or project after mvn package).
setlocal
set "JAR="
for %%f in ("%~dp0..\currency-converter-*.jar" "%~dp0..\target\currency-converter-*.jar") do if not defined JAR set "JAR=%%f"
if not defined JAR (
  echo currency-converter jar not found. Run 'mvn package' first. 1>&2
  exit /b 1
)
javaw -jar "%JAR%" %*
