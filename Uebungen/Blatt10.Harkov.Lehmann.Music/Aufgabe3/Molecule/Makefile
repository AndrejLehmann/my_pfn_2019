.PHONY:test
test:
	@./mol2iter.py molecules.mol2 | diff -w - molecule_out.solution.txt
	@echo "Congratulation. Test passed"
