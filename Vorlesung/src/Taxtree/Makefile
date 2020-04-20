SFX=py

test:test-format
	./test-parse.sh ${SFX} `ls *.tre`
	./splitintolines_test.sh `ls *.tre`

test-format:bacteria.tre bacteria_ids.tre bacteria-stat.txt sampled-pairs-lca.txt sampled-pairs-ids-lca-len.txt subtree test-xml
	./newick_parse.${SFX} --lca sampled-pairs-lca.txt bacteria.tre | \
                         diff - sampled-pairs-lca.txt
	cut -f 1,2,3 sampled-pairs-ids-lca.txt > sampled-pairs-ids-lca-1-3.txt
	./newick_parse.${SFX} --lca sampled-pairs-ids-lca.txt bacteria_ids.tre |\
                         diff - sampled-pairs-ids-lca-1-3.txt
	${RM} sampled-pairs-ids-lca-1-3.txt
	./newick_parse.${SFX} --lca sampled-pairs-ids-lca.txt --path bacteria_ids.tre |\
                         diff - sampled-pairs-ids-lca.txt
	./newick_parse.${SFX} --lca sampled-pairs-ids-lca.txt --path_length bacteria_ids.tre | diff - sampled-pairs-ids-lca-len.txt
	./newick_parse.${SFX} -n bacteria.tre | diff - $<
	./newick_parse.${SFX} -x bacteria.tre | xmllint --noout -
	./newick_parse.${SFX} -c bacteria.tre | diff - bacteria-stat.txt

test-xml:./xml_taxtree_lca.py
	./xml_taxtree_lca.py Tenericutes.sample Tenericutes.xml | diff - Tenericutes.sample

subtree:bacteria.tre subtree-S.txt subtree-B.txt
	./newick_parse.${SFX} --subtree Scytonemataceae -t $< | diff - subtree-S.txt
	./newick_parse.${SFX} --subtree Brasilonema -y $< | diff - subtree-B.txt

search:bacteria.tre Taxaintestdata.txt
	./newick_parse.${SFX} -f ${TAXAFILES} $<

ecoli.xml:bacteria.tre
	./newick_parse.${SFX} --subtree Escherichia_coli -x $< > $@

Tenericutes.xml:bacteria.tre
	./newick_parse.${SFX} --subtree Tenericutes -x $< > $@

.PHONY:clean
clean:
	${RM} sampled-pairs-ids-lca-1-3.txt ecoli.xml
