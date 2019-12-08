.PHONY:test
test:
	@for pnum in 1 2 3 4; do \
                ./gen_email.py email_template.txt patient$$pnum.tsv | diff - email$$pnum.txt;\
	done
	@echo "Congratulations. Tests passed."

clean:
