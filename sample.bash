#!/bin/bash
LD_LIBRARY_PATH=~/usr/lib:/home/grad/samee1/packages/gsl-1.14/lib
export LD_LIBRARY_PATH
BASE=.
DATA=$BASE/data
SRC=$BASE/src
OUTFILE="ind_model.out"
PAR_DIR=$BASE/par
LOG=$BASE/log
OUT=$BASE/out

NSAMPLES=2000

for sample in $(seq ${NSAMPLES})
do

	python pysrc/make_sampled_input.py $DATA/factor_expr_$sample.tab $DATA/dperk_$sample.tab /dev/null

	$SRC/seq2expr -s $DATA/seqs_ind.fa -rs $DATA/r_seqs.fa -e $DATA/expr.tab -m $DATA/factors.wtmx -f $DATA/factor_expr_$sample.tab -o Direct -oo SSE -fo $OUT/ind_$sample.out -na 0 -i $DATA/factor_info.txt -p $PAR_DIR/optimized.par -ct 25 -c $DATA/coop.txt -rt 250 -ff $DATA/free_fix.txt -ft $DATA/factor_thr.txt -dp $DATA/dperk_$sample.tab > $LOG/sample_$sample.log
done
