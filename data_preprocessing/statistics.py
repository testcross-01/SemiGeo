def create_word_set_from_file(file_path):
    """
    读取一个文件，其中每行是一个词，并返回一个词集合。
    """
    with open(file_path, 'r') as file:
        word_set = set(line.strip() for line in file)
    return word_set

def create_word_list_from_file(file_path):
    """
    将分词文件转换为词列表
    """
    word_list=[]
    with open(file_path, 'r') as file:
        for line in file:
           words = line.split(' ')
           for word in words:
               if word != ' ' or word != '':
                  if len(word)>5:
                    word_list.append(word)
            

    return word_list

def count_words_in_set(word_list, word_set):
    """
    统计一个文件中的词有多少在给定的词集合中，以及多少不在。
    返回一个元组 (count_in_set, count_not_in_set)。
    """
    count_in_set = 0
    count_not_in_set = 0

   
    for word in word_list:
         word = word.strip()
         if word in word_set:
                count_in_set += 1
         else:
                count_not_in_set += 1

    return count_in_set, count_not_in_set
train_set= create_word_list_from_file('/home/testcross/projects/WMSeg/data_preprocessing/mydata/larger/train.seg')
word_list = create_word_list_from_file('/home/testcross/projects/WMSeg/data_preprocessing/mydata/larger/train_seg.unseg')
word_set = create_word_set_from_file('/home/testcross/projects/WMSeg/models/bert_wm_av_3_score_0.7_0.8_2024-12-24-11-03-25/geo_words.txt')
count_in_set, count_not_in_set=count_words_in_set(word_list,train_set)
print((count_in_set,count_not_in_set))
#word_set=create_word_set_from_file('/home/testcross/projects/WMSeg/models/bert_wm_av_3_score_0.7_0.8_2024-12-24-11-03-25/geo_words.txt')
#count_words_in_set()
# 示例用法：
# 假设新词表文件的路径是 'new_wordlist.txt'
# count_in_set, count_not_in_set = count_words_in_set('new_wordlist.txt', word_set)
# print(f"在集合中的词数量: {count_in_set}, 不在集合中的词数量: {count_not_in_set}")

# 注意：这段代码假设文件 'new_wordlist.txt' 存在并且格式正确。
