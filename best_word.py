from joblib import Parallel, delayed
from wordfreq import word_frequency

def load_words():
    with open('allowed_words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def not_present(x,a):
    flag=0
    for b in a:
        if (b in x):
            flag=flag+1
            return flag
    return flag
    
def present(x,a):
    flag=0
    for b in a:
        if (b not in x):
            flag=flag+1
            return flag
    return flag

def wrong_position(x,a):
    flag=0
    for b in a:
        if(x[b] in a[b]):
            flag= flag+1
            return flag
    return flag

def right_position(x,a):
    flag=0
    for b in a:
        if(a[b]!=x[b]):
            flag= flag+1
            return flag
    return flag

def simulator(word,x,p,np,rp,wp):
    i=0
    for y in x:
        if (y in word):
            p.add(y)
            if (y==word[i]):
                rp.update({i:y})
            else:
                wp.update({i:y})
        else:
            np.add(y)
        i=i+1
    
            
        

def generator(x):
    
    x.lower()
    count=0
    for y1 in wordle:
        y=y1.lower()
        np=set()
        p=set()
        wp={}
        rp={}
        simulator(y,x,p,np,rp,wp)
        #print(x1,y1,p,np,rp,wp)
        #print(x)
        for z1 in wordle:
            flag=0
            #print(len(wordle1))
            z=z1.lower()
            flag=flag+not_present(z,np)
            if (flag>0):
                count=count+freq_word[z]
                continue
            flag=flag+present(z,p )
            if (flag>0):
                count=count+freq_word[z]
                continue
            flag=flag+wrong_position(z, wp )
            if (flag>0):
                count=count+freq_word[z]
                continue
            flag=flag+right_position(z, rp)
            if (flag>0):
                count=count+freq_word[z]
                continue
    #print(x)
    return x,count       

    

english_words = load_words()
wordle=set()
for x in english_words:
    if len(x)==5:
        wordle.add(x)
print(len(wordle))
freq_word={}
for x in wordle:
    freq_word.update({x:word_frequency(x,'en',wordlist='best')})
    #freq_word.update({x:1})


result=Parallel(n_jobs=64)(delayed(generator)(x) for x in wordle)

    

