#bert softmax
#train
bert_model_path=/opt/Projects/Python/WMSeg/models/Zen
var_decoder=softmax
var_lambda_rate=0.8
var_model_name=zen_memory_cnn_softmax_$var_lambda_rate
python my_wmseg_main.py   --do_train --train_data_path=./data/mydata/larger/train.tsv --eval_data_path=./data/mydata/larger/test.tsv --use_zen --bert_model=$bert_model_path  --decoder=$var_decoder --max_seq_length=3  --decoder=softmax --max_seq_length=300 --max_ngram_size=300 --train_batch_size=16 --eval_batch_size=16 --num_train_epochs=50 --warmup_proportion=0.1 --learning_rate=1e-5 --ngram_num_threshold=2 --patient=10 --ngram_flag=av --av_threshold=3 --model_name=$var_model_name


for i in 1 2 3 4 5
do
var_model_name=i_$var_model_name
CHECKPOINT_PATH=$(cat ./models/model_path.txt)

#predict
python my_wmseg_main.py --do_predict_uc --input_file=./data_preprocessing/mydata/larger/train.unseg --output_file=./data_preprocessing/mydata/larger/self_train.txt --output_file_tsv=./data_preprocessing/mydata/larger/self_train.tsv --eval_model=$CHECKPOINT_PATH --eval_batch_size=16

#self train
python my_wmseg_main.py --use_cnn  --do_train --self_train_data_path=./data_preprocessing/mydata/larger/self_train.tsv --lambda_rate=$var_lambda_rate --train_data_path=./data/mydata/larger/train.tsv --eval_data_path=./data/mydata/larger/test.tsv --use_zen --bert_model=$bert_model_path --decoder=$var_decoder --max_seq_length=300 --max_ngram_size=300 --train_batch_size=16 --eval_batch_size=16 --num_train_epochs=50 --warmup_proportion=0.1 --learning_rate=1e-5 --ngram_num_threshold=2 --patient=10 --ngram_flag=av --av_threshold=3 --model_name=self_$var_model_name

done