from pyamaze import maze, agent


M = maze(10, 10)
M.CreateMaze()


A = agent(M,10, 10, footprints=True)  # Start position (1, 1)
M.enableArrowKey(A)

current_position = A.position
print("Current position of agent A:", current_position)

M.run()  # Run the maze simulation
if A.position == (1, 1):
    print("Winner!")
else:
    print("Did not finished")