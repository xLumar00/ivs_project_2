#!/bin/bash

#========================================
#Directories
#========================================
INSTALL_DIR="/opt/ivs_calc"
BIN_DIR="/usr/local/bin"
DESKTOP_FILE="/usr/share/applications/ivs-calculator.desktop"

#========================================
#Checking permissions (Effective user ID)
#========================================
if [ $EUID -ne 0 ]; then
	echo "A higher permissions required to run."
	exit 1
fi

#========================================
#Copy source
#========================================
mkdir -p "$INSTALL_DIR"
cp -r ../src/* "$INSTALL_DIR"

#========================================
#Copy assets (icon)
#========================================
if [ -d "../assets" ]; then
	cp -r ../assets/* "$INSTALL_DIR/"
fi

#========================================
#Symlink
#========================================
chmod +x "$INSTALL_DIR/main.py"
ln -s -f "$INSTALL_DIR/main.py" "$BIN_DIR/Calculator_IVS"

#========================================
#Check for py3
#========================================
if ! command -v python3 &>/dev/null; then
	echo "python3 is not installed."

	#Instalation suggestion python3
	read -p "Install python3 now? (y/n): " choice
	if [ "$choice" == "y" ]; then
		apt update && apt install python3 -y
	else
		echo "Installation cancelled."
		exit 1
	fi
fi

#========================================
#Check for tkinter
#========================================
if ! python3 -c "import tkinter" &>/dev/null; then
	echo "Missing tkinter (python-tk) library."

	#Instalation suggestion tkinter
	read -p "Install tkinter now? (y/n): " choice
	if [ "$choice" == "y" ]; then
		apt install python3-tk -y
	else
		echo "Installaton cancelled."
		exit 1
	fi
fi

#========================================
#Desktop launcher and icon
#========================================
cat <<EOF >"$DESKTOP_FILE"
[Desktop Entry]
Type=Application
Name=IVS Calculator
Exec=Calculator_IVS
Icon=$INSTALL_DIR/icon.png
Terminal=false
EOF
#========================================

echo "Installation successful!"

