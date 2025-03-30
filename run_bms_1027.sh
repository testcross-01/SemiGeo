#bert softmax
#train

bert_model_path=/opt/Projects/Python/WMSeg/models/Zen
var_decoder=crf
var_model_name=zen_memory_crf


python my_wmseg_main.py  --use_memory --do_train --train_data_path=./data/mydata/larger/train.tsv --eval_data_path=./data/mydata/larger/dev.tsv --use_zen --bert_model=$bert_model_path  --decoder=$var_decoder --max_seq_length=3   --max_seq_length=300 --max_ngram_size=300 --train_batch_size=16 --eval_batch_size=16 --num_train_epochs=50 --warmup_proportion=0.1 --learning_rate=1e-5 --ngram_num_threshold=2 --patient=10 --ngram_flag=av --av_threshold=3 --model_name=$var_model_name

