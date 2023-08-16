import re

def stat_all(tsv_file,rsult_file):
    words_txt='tool/words.txt'
    geo_words_txt='tool/geo_words.txt'
    wrong_words_txt='tool/wrong_words.txt'
    wrong_geo_words_txt='tool/wrong_geo_words.txt'
    dict_path='data/normal_words.txt'
    count=tsv2txt(tsv_file,words_txt)
    geo_count=stat_geo_entity(words_txt,dict_path,geo_words_txt)
    stat_wrong_word(rsult_file,wrong_words_txt)
    wrong_geo_count=stat_geo_entity(wrong_words_txt,dict_path,wrong_geo_words_txt)
    Rgeo= (geo_count-wrong_geo_count)/float(geo_count)
    return count,geo_count,wrong_geo_count,Rgeo


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
                    if word!='':
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
    train_en_count= stat_entity('/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/train.txt')
    train_ge_count=stat_geo_entity_count('/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/train.txt','/opt/Projects/Python/WMSeg/data/normal_words.txt')
    test_en_count= stat_entity('/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/test.txt')
    test_ge_count=stat_geo_entity_count('/opt/Projects/Python/WMSeg/data_preprocessing/mydata/large/test.txt','/opt/Projects/Python/WMSeg/data/normal_words.txt')
    print(train_en_count,train_ge_count,test_en_count,test_ge_count)
    #print(count,geo_countstat_all,wrong_geo_count)