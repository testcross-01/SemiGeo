from my_wmseg_eval import eval_sentence, cws_evaluate_word_PRF, cws_evaluate_OOV,cws_evaluate_geo

def read_all_labels_from_tsv(file_path):
    labels=[]
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                char, label = line.split('\t')  # 假设文字和标签是用制表符分隔的
                labels.append(label)

    return labels;


def read_sentences_from_tsv(file_path):
    sentences = []
    current_sentence = []
    labels_lists= []
    current_labels = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                if(len(line.split('\t'))==1):
                    continue;
                char, label = line.split('\t')  # 假设文字和标签是用制表符分隔的
                current_sentence.append(char)
                current_labels.append(label)
            else:
                if current_sentence:
                    sentences.append(current_sentence)
                    labels_lists.append(current_labels)
                    current_sentence = []
                    current_labels = []


    # 检查文件结束时的最后一个句子是否被添加
    if current_sentence:
        sentences.append(current_sentence)
    if current_labels:
        labels_lists.append(current_labels)
    return  sentences,labels_lists


def test_eval():
    y_preds=['B','E','S','B','I','E']
    y_trues=['B','E','S','B','E','E']
    y_preds_list=[['B','I','I','I','I','I','E']]
    y_trues_list=[['B','I','I','I','I','I','E']]
    sentence_list=[['钙质泥质白云岩']]
    P, R, F=cws_evaluate_word_PRF(y_preds,y_trues)
    print(P, R, F)
    fgeo, rgeo, pgeo= cws_evaluate_geo(y_preds_list,y_trues_list,sentence_list)
    #print(fgeo,rgeo,pgeo)

if __name__ == '__main__':
    # 调用函数并传入文件路径
    true_lables_file_path = 'D:\\testcross\\Downloads\\fsdownload\\test.tsv'
    pred_lables_file_path = 'D:\\testcross\\Downloads\ChromeDownload\\annotated_test_content.tsv'

    sentences,true_labels_lists =read_sentences_from_tsv(true_lables_file_path)
    sentences,pred_labels_lists =read_sentences_from_tsv(pred_lables_file_path)

    y_trues = read_all_labels_from_tsv(true_lables_file_path)
    y_preds = read_all_labels_from_tsv(pred_lables_file_path)
    P, R, F = cws_evaluate_word_PRF(y_preds,y_trues)
    fgeo, rgeo, pgeo = cws_evaluate_geo(pred_labels_lists,true_labels_lists,sentences)
    print(f"Precision (P): {P:.4f}")
    print(f"Recall (R): {R:.4f}")
    print(f"F1-Score (F): {F:.4f}")
    print(f"Precision (P)-GEO: {fgeo:.4f}")
    print(f"Recall (R)-GEO: {rgeo:.4f}")
    print(f"F1-Score (F)-GEO: {pgeo:.4f}")


# Precision (P): 0.5031
# Recall (R): 0.4942
# F1-Score (F): 0.4986
# Precision (P)-GEO: 0.0161
# Recall (R)-GEO: 0.0295
# F1-Score (F)-GEO: 0.0111