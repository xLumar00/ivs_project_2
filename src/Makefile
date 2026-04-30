#========================================
#Variables
#========================================
PYTHON = python3
LOGIN = xluptam00_xlukott00_xheldim00_xvojtat00

#========================================
#Directories
#========================================
MAIN = main.py
TESTS = test_math_lib.py
STDDEV = stddev.py
ROOT = ..
DOC_OUT = $(ROOT)/doc
INSTALL_SRC = $(ROOT)/install
#========================================
.PHONY: all run test doc clean pack help stddev install uninstall

#========================================
#Default commands
#========================================
all:
	@#@$(PYTHON) -m pip --version > /dev/null 2>&1 || (echo "Pip missing. Installing..." && sudo apt update && sudo apt install python3-pip -y)
	$(PYTHON) -m pip install --user -r $(ROOT)/requirements.txt --break-system-packages

#========================================
run:
	$(PYTHON) $(MAIN)

#========================================
test:
	$(PYTHON) $(TESTS)

#========================================
doc:
	@#@command -v doxygen > /dev/null 2>&1 || (echo "Doxygen missing. Installing..." && sudo apt update && sudo apt install doxygen -y)
	cd $(ROOT) && doxygen src/Doxyfile

#========================================
stddev:
	@#$(PYTHON) stddev_num_generator.py | $(PYTHON) $(STDDEV)
	chmod +x $(STDDEV)

#========================================
clean:
	rm -rf __pycache__
	rm -rf $(ROOT)/doc
	rm -rf $(ROOT)/$(LOGIN).zip
	rm -rf $(ROOT)/$(LOGIN)

#========================================
#Packing
#========================================
pack: clean doc
	#Structure creation
	mkdir -p $(ROOT)/$(LOGIN)/repo $(ROOT)/$(LOGIN)/doc $(ROOT)/$(LOGIN)/install

	#Copy everything, one at a time, to avoid looping files and duplicates
	cp -r $(ROOT)/src $(ROOT)/assets $(ROOT)/mockup $(ROOT)/plan $(ROOT)/profiling $(ROOT)/$(LOGIN)/repo/ 2>/dev/null || true
	cp $(ROOT)/.gitignore $(ROOT)/.editorconfig $(ROOT)/LICENSE $(ROOT)/README.md $(ROOT)/*.png $(ROOT)/*.jpg $(ROOT)/*.txt $(ROOT)/*.pdf $(ROOT)/requirements.txt $(ROOT)/$(LOGIN)/repo/ 2>/dev/null || true
	
	#Copy .git files (git history required), -rf
	cp -rf $(ROOT)/.git $(ROOT)/$(LOGIN)/repo/ 2>/dev/null || true

	#Copy install and documentation
	cp -r $(ROOT)/doc/* $(ROOT)/$(LOGIN)/doc/ 2>/dev/null || true
	cp -r $(ROOT)/install/* $(ROOT)/$(LOGIN)/install/ 2>/dev/null || true

	#Clear login inside repo/src clone
	rm -rf $(ROOT)/$(LOGIN)/repo/src/$(LOGIN)

	#Zip and clean
	cd $(ROOT) && zip -r $(LOGIN).zip $(LOGIN)
	rm -rf $(ROOT)/$(LOGIN)

#========================================
#Help
#========================================
help:
	@echo "========================================"
	@echo "        IVS CALCULATOR - Projekt 2"
	@echo "========================================"
	@echo "Autori: $(LOGIN)"
	@echo ""
	@echo "Dostupné príkazy:"
	@echo "  make all    - Nainštaluje závislosti (pip)"
	@echo "  make run    - Spustí grafické rozhranie kalkulačky"
	@echo "  make test   - Spustí automatické testy"
	@echo "  make stddev - Pripraví program pre profiling (nastaví práva)"
	@echo "  make doc    - Vygeneruje programovú dokumentáciu"
	@echo "  make clean  - Odstráni všetky vygenerované súbory"
	@echo "  make pack   - Zabalí projekt do archívu na odovzdanie"
	@echo "========================================"
	
#========================================
#Install/Uninstall
#========================================
install:
	sudo bash $(ROOT)/install/install.sh

#========================================
uninstall:
	sudo bash $(ROOT)/install/uninstall.sh

#========================================
