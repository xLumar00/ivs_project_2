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
	echo "A higher permissions required."
	exit 1
fi
#========================================

echo "Uninstall in progress..."

#========================================
#Uninstalling
#========================================
rm -rf "$INSTALL_DIR"
rm -f "$BIN_DIR/stddev"
rm -f "$BIN_DIR/Calculator_IVS"
rm -f "$DESKTOP_FILE"
#========================================

echo "Calculator_IVS successfuly uninstalled."
