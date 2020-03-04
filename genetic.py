import random
import numpy as np
from prettytable import PrettyTable
import pylab
from mpl_toolkits.mplot3d import Axes3D


def function(x,y):
    func=np.cos(x)*np.cos(y)
    return func


def selection(person,x,y):
    person2=[]
    x2=[]
    y2=[]
    rate=[0]*4
    for i in range(4):
        rate[i] = person[i] / np.sum(person)
    #print(rate)
    for i in range(4):
        proc=random.uniform(min(rate), max(rate))
        ch = 0
        counter = 1
        for j in range(4):
            ch+=person[j]
            if proc<=ch and person[j] not in person2 and counter==1:
                person2.append(person[j])
                x2.append(x[j])
                y2.append(y[j])
                counter-=1

    return person2, x2, y2


def crossover(person,x,y):
    for i in range(4-len(person)):
        k1=random.randint(0, len(person)-1)
        k2=random.randint(0, len(person)-1)
        x.append(x[k1])
        y.append(y[k2])
        person.append(function(x[k1], y[k2]))
    return person, x, y


def mutation(person, x, y):
    proc = random.random()
    mut = 0.75
    if proc > mut:
        x[0], y[0] = y[0], x[0]
    proc = random.random()
    if proc > mut:
        x[1], y[1] = y[1], x[1]
    proc = random.random()
    if proc > mut:
        x[2], y[2] = y[2], x[2]
    proc = random.random()
    if proc > mut:
        x[3], y[3] = y[3], x[3]

    return person, x, y


def fit(x,y,person):
    k=0
    while k < 10:
        p = PrettyTable(["№ поколения", "X", "Y", "Fit", "Max(fit)", "Сред(fit)"])
        for i in range(4):
            if i==0:
                p.add_row([k, "%.4f"%x[i], "%.4f"%y[i], "%.4f"%person[i], "%.4f"%max(person), "%.4f"%np.mean(person)])
            else:
                p.add_row([k, "%.4f"%x[i], "%.4f"%y[i], "%.4f"%person[i], "", ""])
        print(p)

        person, x, y =selection(person,x,y)
        person, x, y =crossover(person,x,y)
        person, x, y =mutation(person,x,y)
        k += 1
        graph(x, y)
    return 0


def makeData():
    x = np.arange (-2, 2, 0.1)
    y = np.arange (-2, 2, 0.1)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = np.cos(xgrid) * np.cos(ygrid)
    return xgrid, ygrid, zgrid


def graph(xfit,yfit):

    x, y, z = makeData()
    fig = pylab.figure()
    axes = Axes3D(fig)
    axes.plot_surface(x, y, z)

    pylab.annotate("1", xy=(0.4210 / 100, -0.3954 / 100), xytext=(20, 20), textcoords='offset points',
                   arrowprops=dict(arrowstyle='->'))
    pylab.annotate("2", xy=(0.4210 / 100, -0.3954 / 100), xytext=(20, 20), textcoords='offset points',
                   arrowprops=dict(arrowstyle='->'))
    pylab.annotate("3", xy=(-0.3954/ 100, 0.4210 / 100), xytext=(20, 20), textcoords='offset points',
                   arrowprops=dict(arrowstyle='->'))
    pylab.annotate("4", xy=(0.4210 / 100, -0.3954 / 100), xytext=(20, 20), textcoords='offset points',
                   arrowprops=dict(arrowstyle='->'))

    pylab.title('Рубежный контроль')
    pylab.ylabel('Y')
    pylab.xlabel('X')
    pylab.show()
    return 0

x=[0]*4
y=[0]*4
person=[0]*4
for i in range(4):
    x[i]=random.uniform(-2, 2)
    y[i]=random.uniform(-2, 2)
    person[i]=function(x[i], y[i])
fit(x, y, person)

