import os.path
import re
import datetime
from zhon.hanzi import punctuation

now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

def word_clean(input_path,output_path):
    word_set=set()
    with open(input_path,'r') as input_file:
        lines= input_file.read().split('\n')
        for line in lines:
            result=re.search('km|km2|^[a-z]+$|m$|米$|%$|[（）]|°|[0-9]个|％',line)
            if result==None:
                word_set.add(line)
    with open(output_path,'w') as output_file:
        for word in word_set:
            output_file.write(word+'\n')

def stat_all(tsv_file,rsult_file,out_dir):

    words_txt=os.path.join(out_dir,'words.txt')

    geo_words_txt=os.path.join(out_dir,'geo_words.txt')
    wrong_words_txt=os.path.join(out_dir,'wrong_words_{0}.txt'.format(now_time))
    wrong_geo_words_txt=os.path.join(out_dir,'wrong_geo_words_{0}.txt'.format(now_time))

    dict_path='data_preprocessing/mydata/geo_words_clear.txt'
    count=tsv2txt(tsv_file,words_txt)
    geo_count=state_word_in_dict(words_txt,dict_path,geo_words_txt)
    stat_wrong_word(rsult_file,wrong_words_txt)
    wrong_geo_count=state_word_in_dict(wrong_words_txt,dict_path,wrong_geo_words_txt)
    Rgeo= (geo_count-wrong_geo_count)/float(geo_count)
    return count,geo_count,wrong_geo_count,Rgeo

def state_word_in_dict(input_file,dict_file,output_file):
    with open(dict_file, 'r') as d:
        words_raw = d.readlines()
        words = []
        output_txt = ''
        count = 0
        for word_rwa in words_raw:
            word = word_rwa.strip()
            words.append(word)
        with open(input_file, 'r') as f:
            input_lines = f.readlines()
            for line in input_lines:
                line_words = line.split(' ')
                for word in line_words:
                    word = word.strip()
                    if word == '':
                        continue
                    if word  in words:
                        count += 1
                        output_txt += word.strip() + '\n'

        if output_file!=None:
            with open(output_file, 'w') as output:
                output.write(output_txt + 'count:' + str(count))

    return count

def stat_wrong_word(input_file,output_file):
    output_txt=''
    with open(input_file,'r') as input:
        input_lines=input.readlines()
        for line in input_lines:
            if re.search('Wrong',line)!=None:
                if line.split(':')[1].strip()=='':
                    continue
                output_txt+= line.split(':')[1]+' '
    with open(output_file,'w') as output:
        output.write(output_txt)

def stat_entity(input_file):
    count=0
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip()!='':
                words=line.split(' ')
                for word in words:
                    word=word.strip()
                    if word!='' and word not in punctuation:
                        count+=1
    return  count

def stat_geo_entity(input_file,dict_file,output_file):
    with open(dict_file,'r') as d:
        words_raw=d.readlines()
        words=[]
        output_txt=''
        count=0
        for word_rwa in words_raw:
            word=word_rwa.strip()
            words.append(word)
        with open(input_file,'r') as f:
            input_lines=f.readlines()
            for line in input_lines:
                line_words=line.split(' ')
                for word in line_words:
                    word=word.strip()
                    if word=='':
                        continue
                    if word not in words:
                        count+=1
                        output_txt+=word.strip()+'\n'
        with open(output_file,'w') as output:
            output.write(output_txt+'count:'+str(count))

        return  count

def stat_geo_entity_count(input_file,dict_file):
    with open(dict_file,'r') as d:
        words_raw=d.readlines()
        words=[]
        output_txt=''
        count=0
        for word_rwa in words_raw:
            word=word_rwa.strip()
            words.append(word)
        with open(input_file,'r') as f:
            input_lines=f.readlines()
            for line in input_lines:
                line_words=line.split(' ')
                for word in line_words:
                    word=word.strip()
                    if word=='':
                        continue
                    if word not in words:
                        count+=1
                        output_txt+=word.strip()+'\n'


        return  count

def tsv2txt(input_file,output_file):
    count=0
    with open(input_file, 'r') as input:
        input_lines=input.readlines()
        output_txt=''
        for line in input_lines:
            if line.strip()!='':
                output_txt+=line[0]
            else:
                output_txt+='\n'
                continue
            if re.search('E|S',line) != None:
                count+=1
                output_txt+=' '
        with open(output_file,'w') as output:
            output.write(output_txt)
    return count

if __name__ == '__main__':
    #tsv2txt('/opt/Projects/Python/WMSeg/data/mydata/geo/my/test.tsv','/opt/Projects/Python/WMSeg/data/test_unseg.txt')
    #stat_geo_entity('/opt/Projects/Python/WMSeg/data/test_unseg.txt','/opt/Projects/Python/WMSeg/data/words.txt','/opt/Projects/Python/WMSeg/data/geo_words.txt')
    #stat_wrong_word('/opt/Projects/Python/WMSeg/models/self_Zen_memory_crf_2023-07-11-20-25-56/CWS_result.txt','/opt/Projects/Python/WMSeg/data/wrong_words.txt')
    #stat_geo_entity('/opt/Projects/Python/WMSeg/data/wrong_words.txt','/opt/Projects/Python/WMSeg/data/words.txt','/opt/Projects/Python/WMSeg/data/wrong_geo_words.txt')
    #stat_wrong_word('/opt/Projects/Python/WMSeg/models/geo_Zen_memory_crf_2023-08-09-14-13-27/CWS_result.txt','/opt/Projects/Python/WMSeg/data/wrong_words2.txt')
    #stat_geo_entity('/opt/Projects/Python/WMSeg/data/wrong_words2.txt','/opt/Projects/Python/WMSeg/data/words.txt','/opt/Projects/Python/WMSeg/data/wrong_geo_words2.txt')
    #count,geo_countstat_all,wrong_geo_count=stat_all('/opt/Projects/Python/WMSeg/data/mydata/geo/my/test.tsv','/opt/Projects/Python/WMSeg/models/self_Zen_memory_crf_2023-07-11-20-25-56/CWS_result.txt')

    all_path='/opt/Projects/Python/WMSeg/data_preprocessing/mydata/all_doc_1800.seg'
    train_path='/opt/Projects/Python/WMSeg/data_preprocessing/mydata/larger/train.seg'
    test_path='/opt/Projects/Python/WMSeg/data_preprocessing/mydata/larger/test.seg'
    dev_path='/opt/Projects/Python/WMSeg/data_preprocessing/mydata/larger/dev.seg'
    dict_path='/opt/Projects/Python/WMSeg/data_preprocessing/mydata/geo_words_clear.txt'

    all_en_count=stat_entity(all_path)
    all_ge_count=state_word_in_dict(all_path,dict_path,None)
    train_en_count= stat_entity(train_path)
    train_ge_count=state_word_in_dict(train_path,dict_path,None)
    test_en_count= stat_entity(test_path)
    test_ge_count=state_word_in_dict(test_path,dict_path,None)
    dev_en_count=stat_entity(dev_path)
    dev_ge_count=state_word_in_dict(dev_path,dict_path,None)

    print('\n all en: {0} , ge: {1}'.format(all_en_count, all_ge_count))
    print('\n train en: {0} , ge: {1}'.format(train_en_count,train_ge_count))
    print('\n dev en: {0} , ge: {1}'.format(dev_en_count, dev_ge_count))
    print('\n test en: {0} , ge: {1}'.format(test_en_count, test_ge_count))
    #print(count,geo_countstat_all,wrong_geo_count)