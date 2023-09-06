import os
import re
from os import path
import random
import argparse

OUTPUT_DIR = '../data'
if not path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)


class MyPrepro(object):
    def __init__(self):
        self.data_dir = './mydata'
        self.data_dir_dict = {'train': 'training', 'test': 'testing'}

    def shuffle(self,file_path):
        lines=[]
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            text = f.read()
            lines = text.split('\n')
            random.shuffle(lines)
                
        return lines
        
    def se_train_test(self):
        dirs=os.listdir(self.data_dir)
        for file_name in dirs:
            if not os.path.isfile(path.join(self.data_dir,file_name)):
                continue;
            file_path=path.join(self.data_dir,file_name);
            train_data,test_data=self._se_train_test(file_path,7);

            output_train_file = path.join(self.data_dir,self.data_dir_dict['train'], 'train_'+file_name)
            output_test_file =path.join(self.data_dir,self.data_dir_dict['test'],'test_'+file_name)
            self._write_file(train_data, output_train_file)
            self._write_file(test_data,output_test_file)


    def se_train_test1(self,file_path,train_num,dev_num,test_num):
        train = []
        test=[]
        dev=[]
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            
            lines = f.readlines()
            for index in range(len(lines)):
                line=lines[index]
                line=line.split('\n')[0]
                if index<train_num:
                    train.append(line)
                elif index<train_num+test_num:
                    test.append(line)
                elif index<train_num+test_num+dev_num:
                    dev.append(line)
        return train,test,dev
            
    def _se_train_test(self,file_path,thr):

        with open(file_path, 'r', encoding='utf-8-sig') as f:
            train = []
            test=[]
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line == '':
                    continue
                if random.randint(0,9)>thr:
                    test.append(line)
                else:
                    train.append(line)
        return train,test



    def process(self):

        for flag in ['train', 'test']:
            dir_path=path.join(self.data_dir, self.data_dir_dict[flag]);
            file_names=os.listdir(dir_path);
            for file_name in file_names:
                file_path = path.join(self.data_dir, self.data_dir_dict[flag], file_name)
                print('processing: %s' % str(file_path))
                data = self._process_file(file_path)
                output_file_dir = path.join(OUTPUT_DIR, 'mydata')
                if not path.exists(output_file_dir):
                    os.mkdir(output_file_dir)
                output_file_name = file_name+'_'+flag + '.tsv'
                output_file_path = path.join(output_file_dir, output_file_name)
                self._write_file(data, output_file_path)



    @staticmethod
    def _process_file(file_path):
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            data = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line == '':
                    continue
                word_list = re.split('\\s+', line)
                for word in word_list:
                    if len(word) == 1:
                        data.append('%s\t%s' % (word, 'S'))
                    elif len(word) == 2:
                        data.append('%s\t%s' % (word[0], 'B'))
                        data.append('%s\t%s' % (word[1], 'E'))
                    else:
                        data.append('%s\t%s' % (word[0], 'B'))
                        for i in range(1, len(word) - 1):
                            data.append('%s\t%s' % (word[i], 'I'))
                        data.append('%s\t%s' % (word[-1], 'E'))
                data.append('\n')
        return data

    @staticmethod
    def _write_file(data, file_path):
        with open(file_path, 'w', encoding='utf8') as f:
            for line in data:
                f.write(line)
                f.write('\n')



if __name__ == '__main__':
   preprocessor = MyPrepro();
   # preprocessor.se_train_test();
   #preprocessor.process();
   #train,test=preprocessor._se_train_test('/opt/Projects/Python/GeoWeakly/data/南昌多要素-区域地质.seg.ann',6)
   #训练数据
   # preprocessor._write_file(train,'/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/train.txt')
   #
   #train_seg,train_unseg=preprocessor._se_train_test('/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/train.txt',5)
   #preprocessor._write_file(train_seg,'/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/train_seg.txt')
   #preprocessor._write_file(train_unseg,'/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/train_unseg.txt')

   # 测试测试
   # preprocessor._write_file(test,'/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/test.txt')
   #
   #
   #train_data = preprocessor._process_file('/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/train_seg.txt')
   # test_data=preprocessor._process_file('/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/test.txt')
   #
   #preprocessor._write_file(train_data, '/opt/Projects/Python/WMSeg/data/mydata/large/train.tsv')
   # preprocessor._write_file(test_data,'/opt/Projects/Python/WMSeg/data/mydata/large/test.tsv')
   raw_seg_path='/opt/Projects/Python/WMSeg/data_preprocessing/mydata/all_doc.seg'
   shuffle_seg_path='/opt/Projects/Python/WMSeg/data_preprocessing/mydata/all_doc_shuffle.seg'
   train_seg_path='/opt/Projects/Python/WMSeg/data_preprocessing/mydata/larger/train.seg'
   test_seg_path='/opt/Projects/Python/WMSeg/data_preprocessing/mydata/larger/test.seg'
   train_unseg_path='/opt/Projects/Python/WMSeg/data_preprocessing/mydata/larger/train.unseg'
   train_tsv_path='/opt/Projects/Python/WMSeg/data/mydata/larger/train.tsv'
   test_tsv_path='/opt/Projects/Python/WMSeg/data/mydata/larger/test.tsv'

   
   shuffle_lines=preprocessor.shuffle(raw_seg_path)
   preprocessor._write_file(shuffle_lines,shuffle_seg_path)
   train,test,dev=preprocessor.se_train_test1(shuffle_seg_path,100,600,300)
   preprocessor._write_file(train,train_seg_path)
   preprocessor._write_file(test,test_seg_path)
   preprocessor._write_file(dev,train_unseg_path)

   
   train_data=preprocessor._process_file(train_seg_path)
   test_data=preprocessor._process_file(test_seg_path)
   preprocessor._write_file(train_data,train_tsv_path)
   preprocessor._write_file(test_data,test_tsv_path)
   
   
   #self_train_data=preprocessor._process_file('/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/self_train.txt')
   #preprocessor._write_file(self_train_data,'/opt/Projects/Python/WMSeg/data/mydata/large/self_train.tsv')



