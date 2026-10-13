@echo off
setlocal
cd /d "%~dp0"
set "A03PKG=AP_crDroid_10.13_A032M_S7_EXPERIMENTAL"
set "A03ZIP=%ProgramFiles%\7-Zip\7z.exe"
if not exist "%A03ZIP%" set "A03ZIP=%ProgramFiles(x86)%\7-Zip\7z.exe"
if not exist "%A03ZIP%" (
 echo ERRO: 7-Zip nao encontrado.
 exit /b 1
)
for %%N in (001 002 003 004) do if not exist "%A03PKG%.tar.gz.%%N" (
 echo ERRO: falta a parte %%N.
 exit /b 1
)
copy /b "%A03PKG%.tar.gz.001"+"%A03PKG%.tar.gz.002"+"%A03PKG%.tar.gz.003"+"%A03PKG%.tar.gz.004" "%A03PKG%.tar.gz"
if errorlevel 1 exit /b 1
powershell -NoProfile -Command "$ErrorActionPreference='Stop'; if ((Get-FileHash -LiteralPath ($env:A03PKG+'.tar.gz') -Algorithm SHA256).Hash -ne 'fd4181ecdff5e6136fe5d059c8cad511c9200ee267fd8e6ae1f740b356101d3e') {throw 'SHA256 do arquivo compactado diferente'}"
if errorlevel 1 exit /b 1
"%A03ZIP%" t "%A03PKG%.tar.gz"
if errorlevel 1 exit /b 1
"%A03ZIP%" x "%A03PKG%.tar.gz" -aoa
if errorlevel 1 exit /b 1
powershell -NoProfile -Command "$ErrorActionPreference='Stop'; if ((Get-FileHash -LiteralPath ($env:A03PKG+'.tar') -Algorithm SHA256).Hash -ne '8bdc19cfb7105f41ac5a5282b03546c84a4540d42e3aab67c531a0e8d1bd2dd9') {throw 'SHA256 do TAR diferente'}"
if errorlevel 1 exit /b 1
"%A03ZIP%" t "%A03PKG%.tar"
if errorlevel 1 exit /b 1
"%A03ZIP%" l "%A03PKG%.tar"
if errorlevel 1 exit /b 1
echo PACOTE CONFERIDO. Este comando nao grava no celular.
echo AP TAR experimental: %A03PKG%.tar
endlocal
