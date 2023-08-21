from joblib import Parallel, delayed
import json,time

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

def repeat(x,a):
    flag=0
    for b in a:
        if ( x.count(b)<a[b]):
            flag=flag+1
            return flag
    return flag
def strict_repeat(x,a):
    flag=0
    for b in a:
        if (x.count(b)!=a[b]):
            flag=flag+1
            return flag
    return flag

def simulator(word,x,p,np,rp,wp,re,s_re):
    i=0
    for y in x:
        if (y in word):
            p.add(y)
            if (y==word[i]):
                rp.update({i:y})
            else:
                wp.update({i:y})
            if x.count(y)>word.count(y):
                s_re.update({y:word.count(y)})
            else:
                re.update({y:x.count(y)})
            
        else:
            np.add(y)
        i=i+1
    
            
        

def generator(x):
    
    x.lower()
    count=0
    for y1 in wordle1:
        y=y1.lower()
        np=set()
        p=set()
        wp={}
        rp={}
        re={}
        s_re={}
        simulator(y,x,p,np,rp,wp,re,s_re)
        #print(x1,y1,p,np,rp,wp)
        #print(x)
        for z1 in wordle1:
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
            flag=flag+repeat(z, re)
            if (flag>0):
                count=count+freq_word[z]
                continue
            flag=flag+strict_repeat(z, s_re)
            if (flag>0):
                count=count+freq_word[z]
                continue    
    return x,count       


def pattern(x,i):
    y=['b','o','r']
    if(i==5):
        pat.add(x)
        return
    for z in y:
        #print(x)
        temp=list(x)
        temp[i]=z
        x="".join(temp)
        pattern(x,i+1)
 
        

english_words = load_words()
wordle=set()
pat=set()
freq_word={}

for x in english_words:
    if len(x)==5:
        wordle.add(x)
print(len(wordle))

f=open('freq.txt')
freq_word=json.loads(f.read())
    #freq_word.update({x:1})
    
pattern('bbbbb',0)

word='soare'
sec_guess={}
seconds=time.time()
for color in pat:
    wordle1=set(wordle)
    np=set()
    p=set()
    wp={0:set(),1:set(),2:set(),3:set(),4:set()}
    rp={}
    re={}
    s_re={}
    local={}
    for l in word:
        local.update({l:0})
    for i in range(5):
        if (color[i]=='g'):
            rp.update({i:word[i]})
            local.update({word[i]:local[word[i]]+1})
            p.add(word[i])
            
        elif (color[i]=='o'):
            wp[i].add(word[i])
            local.update({word[i]:local[word[i]]+1})
            p.add(word[i])
            
    for i in range(5): 
        if (color[i]=='b'):
            if word[i] not in p:
                np.add(word[i])
            else:
                s_re.update({word[i]:local[word[i]]})
                wp[i].add(word[i])
            
    for l in local:
        if l not in re:
            if local[l]>0:
                re.update({l:local[l]})
        elif local[l]>re[l]:
            re.update({l:local[l]})
 
    for y in wordle:
             x=y
             x.lower()
             flag=0
             flag=flag+not_present(x, np)
             flag=flag+present(x, p)
             flag=flag+wrong_position(x,wp)
             flag=flag+right_position(x, rp)
             flag=flag+repeat(x, re)
             flag=flag+strict_repeat(x, s_re)
             if (flag>0):
                 wordle1.remove(x)
    print(len(wordle1))  

    result=Parallel(n_jobs=64)(delayed(generator)(x) for x in wordle)
    Result={}
    for x in result:
        Result.update({x[0]:x[1]})
    Keymax = max(zip(Result.values(), Result.keys()))[1]
    print(color,Keymax)
    print(time.time()-seconds)
    sec_guess.update({color:Keymax})
with open('second_guess.txt', 'w') as file:
     file.write(json.dumps(sec_guess)) # use `json.loads` to do the reverse  
