#========================================
#Variables
#========================================
PYTHON = python3
LOGIN = xluptam00_xlukott00_xheldim00_xvojtat00

#========================================
#Directories
#========================================
SRC = src
MAIN = $(SRC)/main.py
TESTS = $(SRC)/tests.py

#========================================
.PHONY: all run test doc clean pack help stddev install uninstall

#========================================
#Default commands
#========================================
all:
	pip install -r requirements.txt

#========================================
run:
	$(PYTHON) $(MAIN)

#========================================
test:
	$(PYTHON) $(TESTS)

#========================================
doc:
	doxygen Doxyfile

#========================================
stddev:
	$(PYTHON) profiling/stddev_numgenerator.py | $(PYTHON) $(SRC)/stddev.py

#========================================
clean:
	rm -rf __pycache__
	rm -rf $(SRC)/__pycache__
	rm -rf doc
	rm -rf $(LOGIN).zip

#========================================
#Packing
#========================================
pack: clean doc
	mkdir -p $(LOGIN)/repo
	mkdir -p $(LOGIN)/doc
	mkdir -p $(LOGIN)/install

	#Copy repo including hidden git files
	cp -r . $(LOGIN)/repo/

	rm -rf $(LOGIN)/repo/doc
	rm -rf $(LOGIN)/repo/$(LOGIN)

	cp -r doc/* $(LOGIN)/doc/
	cp -r install/* $(LOGIN)/install/

	#Zip
	zip -r $(LOGIN).zip $(LOGIN)
	rm -rf $(LOGIN)

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
	@echo "  make stddev - Spustí program pre profiling"
	@echo "  make doc    - Vygeneruje programovú dokumentáciu"
	@echo "  make clean  - Odstráni všetky vygenerované súbory"
	@echo "  make pack   - Zabalí projekt do archívu na odovzdanie"
	@echo "========================================"
	
#========================================
#Install/Uninstall
#========================================
install:
	sudo bash install/install.sh

#========================================
uninstall:
	sudo bash install/uninstall.sh

#========================================
