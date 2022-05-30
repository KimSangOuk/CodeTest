def array_rotate(array,direction):
  height=len(array)
  width=len(array[0])

  array_complete=[[0]*height for i in range(width)]

  if direction==True:
    for i in range(height):
      for j in range(width):
        array_complete[j][width-1-i]=array[i][j]
  else:
    for i in range(height):
      for j in range(width):
        array_complete[height-j-1][i]=array[i][j]

  return array_complete