import re
def eval_sentence(y_pred, y, sentence,word2id):
    words = sentence.split(' ')
    seg_pred = []
    label_seg_pred=[]
    word_pred = ''
    label_pred=''
    uncoop_num=0
    if re.findall(' B[IS]+B| I| E',sentence) !=None:
        uncoop_num=len(re.findall(' B[IS]+B| I| E',sentence))
    wrong_num=0

    if y is not None:
        word_true = ''
        seg_true = []

        label_true = ''
        label_seg_true = []

        seg_wrong=[]
        start = 0
        for i in range(len(y)):
            word_true += words[i]
            label_true += y[i]
            if y[i] in ['S', 'E']:
                for j in range(start, i + 1):
                    if y[j] != y_pred[j]:
                        seg_wrong.append(word_true)
                        wrong_num+=1
                        break
                if word_true not in word2id:
                    word_true = '*' + word_true + '*'
                seg_true.append(word_true)
                label_seg_true.append(label_true)
                word_true = ''
                label_true = ''
                #调整start到下一个词
                start=i+1

        label_seg_true_str=' '.join(label_seg_true)
        seg_wrong_str=' '.join(seg_wrong)
        seg_true_str = ' '.join(seg_true)
    else:
        label_seg_true_str = None
        seg_true_str = None
        seg_wrong_str= None


    for i in range(len(y_pred)):
        word_pred += words[i]
        label_pred +=y_pred[i]
        if y_pred[i] in ['S', 'E']:
            seg_pred.append(word_pred)
            label_seg_pred.append(label_pred)
            word_pred = ''
            label_pred = ''
    seg_pred_str = ' '.join(seg_pred)
    label_seg_pred_str=' '.join(label_seg_pred)
    return seg_true_str, seg_pred_str,seg_wrong_str,label_seg_true_str,label_seg_pred_str,wrong_num,uncoop_num


def cws_evaluate_word_PRF(y_pred, y):
    #dict = {'E': 2, 'S': 3, 'B':0, 'I':1}
    cor_num = 0
    yp_wordnum = y_pred.count('E')+y_pred.count('S')
    yt_wordnum = y.count('E')+y.count('S')
    start = 0
    for i in range(len(y)):
        if y[i] == 'E' or y[i] == 'S':
            flag = True
            for j in range(start, i+1):
                if y[j] != y_pred[j]:
                    flag = False
            if flag:
                cor_num += 1
            start = i+1

    P = cor_num / float(yp_wordnum) if yp_wordnum > 0 else -1
    R = cor_num / float(yt_wordnum) if yt_wordnum > 0 else -1
    F = 2 * P * R / (P + R)
    print('P: ', P)
    print('R: ', R)
    print('F: ', F)
    return P, R, F


def cws_evaluate_OOV(y_pred_list, y_list, sentence_list, word2id):
    cor_num = 0
    yt_wordnum = 0
    for y_pred, y, sentence in zip(y_pred_list, y_list, sentence_list):
        start = 0
        for i in range(len(y)):
            if y[i] == 'E' or y[i] == 'S':
                word = ''.join(sentence[start:i+1])
                if word in word2id:
                    start = i + 1
                    continue
                flag = True
                yt_wordnum += 1
                for j in range(start, i+1):
                    if y[j] != y_pred[j]:
                        flag = False
                if flag:
                    cor_num += 1
                start = i + 1

    OOV = cor_num / float(yt_wordnum) if yt_wordnum > 0 else -1
    return OOV
