# from pyMaze import maze,agent,COLOR,textLabel
import timeit
from pyamaze import maze,agent,textLabel,COLOR

def DFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSeacrh,dfsPath,fwdPath

if __name__=='__main__':
    m=maze(20,16) # Change to any size
    m.CreateMaze() # (2,4) is Goal Cell, Change that to any other valid cell

    dSeacrh,dfsPath,fwdPath=DFS(m) # (5,1) is Start Cell, Change that to any other valid cell
    
    a=agent(m,footprints=True,color=COLOR.green)
    b=agent(m,footprints=True,filled=True)
    c=agent(m,footprints=True,color=COLOR.yellow)
    m.tracePath({a:dSeacrh},delay=80)
    m.tracePath({b:dfsPath}, delay=80)
    m.tracePath({c:fwdPath}, delay=80)

    # t1=timeit(stmt='DFS(m)',number=1000,globals=globals())
    # textLabel(m,'DFS Time',t1)
    m.run()

    ## The code below will generate the maze shown in video

    # m=maze()

    # dSeacrh,dfsPath,fwdPath=DFS(m)

    # a=agent(m,footprints=True,color=COLOR.green)
    # b=agent(m,1,1,goal=(5,5),footprints=True,filled=True,color=COLOR.cyan)
    # c=agent(m,footprints=True,color=COLOR.yellow)
    # m.tracePath({a:dSeacrh},showMarked=True)
    # m.tracePath({b:dfsPath})
    # m.tracePath({c:fwdPath})
    # m.run()
