import pyautogui
import time

def check_score(lines):
    for i in range(1,len(lines),2):
        try:
            lines[i] = float(lines[i])
        except:
            raise Exception('format of score is worng!')


def analysis_music(path='score.txt'):
    with open(path,'r',encoding='utf-8') as f:
        lines = f.readlines()
    lines = [i.strip() for i in lines if i.strip() != '']
    check_score(lines)
    for i in range(0,len(lines)):
        if i%2 == 0:
            
            lines[i] = lines[i].split('#')
    return lines

def play(score,delay=10):
    dic = {
        'do_h':'q',
        'do_m':'a',
        'do_l':'z',
        're_h':'w',
        're_m':'s',
        're_l':'x',
        'mi_h':'e',
        'mi_m':'d',
        'mi_l':'c',
        'fa_h':'r',
        'fa_m':'f',
        'fa_l':'v',
        'so_h':'t',
        'so_m':'g',
        'so_l':'b',
        'la_h':'y',
        'la_m':'h',
        'la_l':'n',
        'ti_h':'u',
        'ti_m':'j',
        'ti_l':'m'
    }
    time.sleep(delay)
    for i in range(0,len(score)):
        if i%2 == 0:
            print([dic[j] for j in score[i]])
            pyautogui.press([dic[j] for j in score[i]])
        else:
            time.sleep(score[i])
    pass

lines = analysis_music('score.txt')     # your score file  乐谱文件
play(lines,5)                           # first argument is fixable, don't change it, second argument is the delay time.
                                        # 第一个参数是固定的，别改。第二个参数是延迟时间 