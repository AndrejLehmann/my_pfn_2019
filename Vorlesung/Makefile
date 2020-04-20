.PHONY:ausgelassen
ausgelassen:
	@grep '\-\-' README | cut -f 2 -d ',' | sed 's/^[ ]*//' | awk -F '--' '{sum+=$$2-$$1+1} END{print sum}'
