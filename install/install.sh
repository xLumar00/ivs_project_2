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
#Checking pip
#========================================
if ! command -v pip3 &>/dev/null; then
	apt update && apt install python3-pip -y
fi
python3 -m pip install customtkinter --break-system-packages

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
#Copy source and Uninstall script
#========================================
mkdir -p "$INSTALL_DIR"
cp -r ../src/* "$INSTALL_DIR"
cp ../install/uninstall.sh "$INSTALL_DIR/uninstall.sh"
chmod +x "$INSTALL_DIR/uninstall.sh"

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
#ln -s -f "$INSTALL_DIR/main.py" "$BIN_DIR/Calculator_IVS"

#main wrapper:
cat <<EOF >"$BIN_DIR/Calculator_IVS"
#!/bin/bash
cd $INSTALL_DIR
python3 main.py "\$@"
EOF
chmod +x "$BIN_DIR/Calculator_IVS"

#========================================
# Symlink pre stddev (profiling)
#========================================
chmod +x "$INSTALL_DIR/stddev.py"
#ln -s -f "$INSTALL_DIR/stddev.py" "$BIN_DIR/stddev"

#stddev wrapper
cat <<EOF >"$BIN_DIR/stddev"
#!/bin/bash
cd $INSTALL_DIR
python3 stddev.py "\$@"
EOF
chmod +x "$BIN_DIR/stddev"

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
