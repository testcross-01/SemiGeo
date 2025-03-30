# GeoCWS

## Requirements

Our code works with the following environment.
* `python=3.6`
* `pytorch=1.1`

## Downloading BERT, ZEN

In our paper, we use BERT ([paper](https://www.aclweb.org/anthology/N19-1423/)) and ZEN ([paper](https://arxiv.org/abs/1911.00720)) as the encoder.

For BERT, please download pre-trained BERT-Base Chinese from [Google](https://github.com/google-research/bert) or from [HuggingFace](https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese.tar.gz). If you download it from Google, you need to convert the model from TensorFlow version to PyTorch version.

For ZEN, you can download the pre-trained model from [here](https://github.com/sinovation/ZEN).

## Datasets

Geo数据集放置在data/mydata/larger中，train.tsv、test.tsv和dev.tsv分别对应着训练集、测试集和开发集，train.unseg对应的未标注数据,self-train.tsv 为伪标签数据（会随着迭代而变化）

## Training and Testing

训练代码的脚本可以参考run_bms_1205.sh

Here are some important parameters:

* `--do_train`: train the model.
* `--self_train_data_path`: 自训练的伪标签数据位置（tsv）
* `--lambda_rate`: 自训练伪标签筛选阈值（0-1）
* `--do_test`: test the model.
* `--use_bert`: use BERT as encoder.
* `--use_zen`: use ZEN as encoder.
* `--bert_model`: the directory of pre-trained BERT/ZEN model.
* `--use_memory`: use key-value memory networks.
* `--decoder`: use `crf` or `softmax` as the decoder.
* `--ngram_flag`: use `av`, `dlg`, or `pmi` to construct the lexicon N.
* `--av_threshold`: when using `av` to construct the lexicon N, n-grams whose AV score is lower than the threshold will be excluded from the lexicon N.
* `--ngram_num_threshold`: n-grams whose frequency is lower than the threshold will be excluded from the lexicon N. Note that, when the threshold is set to 1, no n-gram is filtered out by its frequency. We therefore **DO NOT** recommend you to use 1 as the n-gram frequency threshold.
* `--model_name`: the name of model to save.

## Predicting

Here are some important parameters:

* `--do_predict`: segment the sentences using a pre-trained WMSeg model.
* `--do_predict_uc`:基于不确定性感知的伪标签生成
* `--output_file_tsv`：伪标签tsv文件输出位置
* `--input_file`: the file contains sentences to be segmented. Each line contains one sentence; you can refer to [a sample input file](./sample_data/sentence.txt) for the input format.
* `--output_file`: the path of the output file. Words are segmented by a space.
* `--eval_model`: the pre-trained WMSeg model to be used to segment the sentences in the input file.

## LLM-GeoCWS

此模块主要是ChatGPT文件夹中chatgpt_cws.py部分，cws_rag()为利用rag功能提示GPT-4o模型进行分词，cws()为直接利用GPT-4o进行分词。此部分可以将数据增强后的切分文本加到self_train_data_path中的数据之后以扩充数据集，此部分与前面几个部分并未做整合，需要单独创建一个python的虚拟环境（openai 1.52.0与pytorch1.1存在冲突）。

* python 3.9.20
* pymilvus 2.5.2
* openai 1.52.0
* torch 2.5.1

