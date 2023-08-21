def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def not_present(x,a):
    flag=0
    for b in a:
        if (b in x):
            flag=flag+1
    return flag
    
def present(x,a):
    flag=0
    for b in a:
        if (b not in x):
            flag=flag+1
    return flag

def wrong_position(x,a):
    flag=0
    for b in a:
        if(x[b] in a[b]):
            flag= flag+1
    return flag

def right_position(x,a):
    flag=0
    for b in a:
        if(a[b]!=x[b]):
            flag= flag+1
    return flag

def letter_count(wordle1):
    count={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for x in wordle1:
        for y in count:
            if(y in x):
                count[y]=count[y]+1
    return count

if __name__ == '__main__':
    english_words = load_words()
    # demo print
    #print('fate' in english_words)
    wordle=set()
    for x in english_words:
        if len(x)==5:
            wordle.add(x)
    print(len(wordle))
    wordle1=set(wordle)
    np={'r','i','s','e'}
    p={'a'}
    wp={0:{'a'},1:{},2:{},3:{},4:{}}
    rp={}
    for y in wordle:
             x=y
             x.lower()
             flag=0
             flag=flag+not_present(x, np)
             flag=flag+present(x, p)
             flag=flag+wrong_position(x,wp)
             flag=flag+right_position(x, rp)
             if (flag>0):
                 wordle1.remove(x)
    print(len(wordle1))   
    count=letter_count(wordle1)
    print(dict(sorted(count.items(), key=lambda item: item[1])))
            