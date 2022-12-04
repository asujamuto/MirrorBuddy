import matplotlib.pyplot as plt
import numpy as np
import json
import os


intents = json.loads(open('/home/pete/Coding/Python/Medi_Bot/Buddy/databases/word_bank2.json').read())

def write_to_file(intents = intents):
    os.remove("documentation2.txt")
    for i in range(len(intents['intents'])):
        print(f"Tag: {intents['intents'][i]['tag']}, Pattern {len(intents['intents'][i]['patterns'])}")
        with open('./documentation2.txt', 'a') as f:
            f.write(f"Tag: {intents['intents'][i]['tag']}, Pattern {len(intents['intents'][i]['patterns'])} \n")
     
def plots():
    xpoints = []
    ypoints = []
    for i in range(len(intents['intents'])):
        xpoints.append(i)
        ypoints.append(len(intents['intents'][i]['patterns']))

    print(xpoints, ypoints)
   
    vector = np.vectorize(np.int_)
    xpoints = np.array([xpoints])
    ypoints = np.array([ypoints])

    xpoints = xpoints.astype(int)
    ypoints = ypoints.astype(int)
    
    print(xpoints, ypoints)
    
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

    plt.title("Number of patterns in each tag", fontdict = font1)
    plt.xlabel("Number of Tag", fontdict = font2)
    plt.ylabel("Number of Patterns", fontdict = font2)
    plt.plot(xpoints, ypoints, marker = 'o')
    plt.show()

    return xpoints, ypoints


def text():
    for i in range(83 - 1):
        with open('./responses.txt', 'a') as f:       
            f.write(f"{intents['intents'][i]['responses']} \n")


write_to_file()

