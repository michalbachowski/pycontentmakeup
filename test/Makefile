testrunner=python -B ./runtest.py
fix_pythonpath=PYTHONPATH="`readlink -f '../src/'`:$$PYTHONPATH"

test:
	$(testrunner)

test_local:
	$(fix_pythonpath) $(testrunner)

coverage_run:
	$(fix_pythonpath) python -B -mcoverage run $(testrunner)

coverage_report:
	python -B -mcoverage report -m

coverage_erase:
	python -B -mcoverage erase

coverage: coverage_erase coverage_run coverage_report
	@echo "DONE"

.PHONY: test test_local coverage_report coverage_erase coverage
