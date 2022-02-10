def solution(map):
   queue = []
   successful_paths = []
   hit_a_wall_list = []
   shortest_path = len(map[0])+len(map)-1

   # add starting point to queue
   queue.append([[len(map[-1])-1, len(map)-1]])

   # check if move is in bounds and wall or free space
   def check_valid_move(point, move, add_wall_outcomes, list_identifier):
       x = point[0][0]
       y = point[0][1]
       if move == "L":
           x -= 1
       elif move == "R":
           x += 1
       elif move == "U":
           y -= 1
       elif move == "D":
           y += 1
       if not (0 <= x < len(map[0]) and 0 <= y < len(map)):
           pass
       elif map[y][x] == 1:
           if add_wall_outcomes == 0:
               if list_identifier == 0:
                   temp_list = [[x, y]]+queue[0]
                   check_for_backwards_moves(temp_list, 1)
               else:
                   temp_list = [[x, y]] + hit_a_wall_list[0]
                   check_for_backwards_moves(temp_list, 1)
       else:
           if list_identifier == 0:
               temp_list = [[x, y]]+queue[0]
               check_for_backwards_moves(temp_list, 0)
           else:
               temp_list = [[x, y]] + hit_a_wall_list[0]
               check_for_backwards_moves(temp_list, 0)
       if list_identifier == 0:
           if queue[-1][0] == [0, 0]:
               successful_paths.append(queue[-1])
           if move == "D":
               queue.pop(0)
       else:
           if queue[-1][0] == [0, 0]:
               successful_paths.append(queue[-1])
           if move == "D":
               hit_a_wall_list.pop(0)

   def check_for_backwards_moves(temp_list, list_gate):
       for elem in temp_list:
           if temp_list.count(elem) > 1:
               return
       if list_gate == 0:
           queue.append(temp_list)
       else:
           hit_a_wall_list.append(temp_list)

   def find_solution():
       for direction in ["L", "R", "U", "D"]:
           check_valid_move(queue[0], direction, 0, 0)

   while len(queue[-1]) < shortest_path:
       find_solution()

   def find_solution_walls():
       for direction in ["L", "R", "U", "D"]:
           check_valid_move(hit_a_wall_list[0], direction, 1, 1)

   while len(successful_paths) == 0:
       find_solution_walls()
   print(len(successful_paths[0]))


solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])