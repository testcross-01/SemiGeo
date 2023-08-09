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


    def se_train_test(self):
        dirs=os.listdir(self.data_dir)
        for file_name in dirs:
            if not os.path.isfile(path.join(self.data_dir,file_name)):
                continue;
            file_path=path.join(self.data_dir,file_name);
            train_data,test_data=self._se_train_test(file_path);

            output_train_file = path.join(self.data_dir,self.data_dir_dict['train'], 'train_'+file_name)
            output_test_file =path.join(self.data_dir,self.data_dir_dict['test'],'test_'+file_name)
            self._write_file(train_data, output_train_file)
            self._write_file(test_data,output_test_file)



    def _se_train_test(self,file_path):

        with open(file_path, 'r', encoding='utf-8-sig') as f:
            train = []
            test=[]
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line == '':
                    continue
                if random.randint(0,9)>7:
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
   data=preprocessor._process_file('/opt/Projects/Python/GeoWeakly/data/my_geo.seg')
   preprocessor._write_file(data,'/opt/Projects/Python/WMSeg/data/mydata/self_traing/train.tsv')

