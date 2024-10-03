#  Team Id : GG_3644
#  Author List : Utkarsh Shivhare, Mudit Agrawal
#  Filename: direction_algo.py
#  Theme: Geo Guide (GG) Theme (eYRC 2023-24)
#  Functions: dijkstra_shortest_path, direction, angle, find_nearest_index, turning_str
#  Global Variables: coordinates, cord, bot_id

import heapq
import math

coordinates = [{'x': 31, 'y': 836}, {'x': 80, 'y': 751}, {'x': 70, 'y': 572}, {'x': 72, 'y': 361}, {'x': 75, 'y': 219}, {'x': 191, 'y': 749}, {'x': 182, 'y': 364}, {'x': 189, 'y': 72}, {'x': 436, 'y': 744}, {'x': 437, 'y': 555}, {'x': 443, 'y': 372}, {'x': 441, 'y': 234}, {'x': 662, 'y': 558}, {'x': 696, 'y': 380}, {'x': 807, 'y': 559}, {'x': 809, 'y': 384}, {'x': 807, 'y': 248}, {'x': 101, 'y': 79},{'x':769,'y':105}]
cord=[{'x': 31, 'y': 836}, {'x': 80, 'y': 751}, {'x': 70, 'y': 572}, {'x': 72, 'y': 361}, {'x': 75, 'y': 219}, {'x': 191, 'y': 749}, {'x': 182, 'y': 364}, {'x': 189, 'y': 72}, {'x': 436, 'y': 744}, {'x': 437, 'y': 555}, {'x': 443, 'y': 372}, {'x': 441, 'y': 234}, {'x': 662, 'y': 558}, {'x': 696, 'y': 380}, {'x': 807, 'y': 559}, {'x': 809, 'y': 384}, {'x': 807, 'y': 248}, {'x': 101, 'y': 79},{'x':769,'y':105}]   
bot_id=100




def dijkstra_shortest_path(graph, start, end):
    # """
    # * Function Name: dijkstra_shortest_path
    #  * Input:
    #     - graph (dict): A dictionary representing the graph where keys are nodes and values are lists of tuples.
    #       Each tuple contains a neighbor node and the distance to that neighbor.
    #     - start: The starting node for finding the shortest path.
    #     - end: The destination node for finding the shortest path.
    #  * Output: 
    #     - path (list or None): A list representing the shortest path from the start node to the end node.
    #       If no path is found, returns None.
    #  * Logic: 
    #     This function implements Dijkstra's algorithm to find the shortest path in a weighted graph.
    #     It takes a graph represented as a dictionary, the starting node, and the destination node as input.
    #     The algorithm maintains a priority queue to explore nodes in order of increasing distance from the start node.
    #     It initializes the distance to each node as infinity and the predecessor of each node as None.
    #     The algorithm iteratively explores nodes and updates their distances and predecessors as it finds shorter paths.
    #     Once the destination node is reached, it reconstructs the shortest path from start to end.
    #  * Example Call: 
    #     graph = {'A': [('B', 1), ('C', 4)],
    #              'B': [('A', 1), ('C', 2), ('D', 5)],
    #              'C': [('A', 4), ('B', 2), ('D', 1)],
    #              'D': [('B', 5), ('C', 1)]}
    #     shortest_path = dijkstra_shortest_path(graph, 'A', 'D')
    #     print(shortest_path)
        
    # Example graph representation:
    
    #     A --1-- B
    #     |       |
    #     4       2
    #     |       |
    #     C --1-- D
    # """
    
    
    # Priority queue to store (distance, node). Starts with the start node at distance 0.
    queue = [(0, start)]
    # Dictionary to keep track of the minimum distance to reach each node.
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Dictionary to track the predecessor of each node along the shortest path.
    predecessors = {node: None for node in graph}

    while queue:
        # Get the node with the smallest distance so far.
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break  # Stop if the end node has been reached.

        # Visit each neighbor of the current node.
        for neighbor, distance in graph[current_node]:
            new_distance = current_distance + distance

            # If a shorter path to the neighbor is found,
            # update the neighbor's distance, set the predecessor, and enqueue it.
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor))

    # Reconstruct the shortest path from start to end.
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()  # Reverse the path to start from the beginning.

    # Return the shortest path
    return path if path[0] == start else None



def direction(x1,y1,x2,y2,bot_angle):
    # """
    #  * Function Name: direction
    #  * Input:
    #     - x1 (float): x-coordinate of the starting point.
    #     - y1 (float): y-coordinate of the starting point.
    #     - x2 (float): x-coordinate of the target point.
    #     - y2 (float): y-coordinate of the target point.
    #     - bot_angle (float): Angle of the bot's orientation in degrees (-180 to 180).
    #  * Output: 
    #     - dir (str): A direction towards which the bot should move ('f' for forward, 'b' for backward, 
    #       'l' for left, 'r' for right).
    #  * Logic: 
    #     This function calculates the direction in which a bot should move from its current position 
    #     to a target position based on the Cartesian coordinates of both positions and the angle of 
    #     the bot's orientation. It determines the direction by comparing the differences in x and y 
    #     coordinates between the current and target positions. Depending on the greater difference 
    #     (x or y), and the orientation angle of the bot, it assigns the appropriate direction.
    #  * Example Call: 
    #     direction(0, 0, 1, 1, 45)
        
    # * Example scenario:
    
    # Let's assume the bot is at position (0, 0) with an orientation angle of 45 degrees.
    # The target position is (1, 1).
    
    # - Since both x and y distances are equal (1 unit each), the function checks the orientation angle.
    #   - If the bot's angle is between -45 and 45 degrees, it should move forward ('f').
    #   - Otherwise, it should move diagonally to the right ('r').
    
    # The function returns 'f' in this example.
    # """
    
    x_dis=abs(x1-x2)
    y_dis=abs(y1-y2)
    if(max(x_dis,y_dis)==x_dis):                   # Logic to determine direction based on x distance
        if(x2>x1):
            if(bot_angle>=-45 and bot_angle<=45):
                return "r"
            elif(bot_angle>=45 and bot_angle<=135):
                return "f"
            elif(bot_angle>=135 or bot_angle<=-135):
                return "l"
            else:
                return "u"
        
        else:
            if(bot_angle>=-45 and bot_angle<=45):
                return "l"
            elif(bot_angle>=45 and bot_angle<=135):
                return "u"
            elif(bot_angle>=135 or bot_angle<=-135):
                return "r"
            else:
                return "f"
    else:                                            # Logic to determine direction based on y distance 
        if(y1>y2):
            if(bot_angle>=-45 and bot_angle<=45):
                return "f"
            elif(bot_angle>=45 and bot_angle<=135):
                return "l"
            elif(bot_angle>=135 or bot_angle<=-135):
                return "u"
            else:
                return "r"
        
        else:
            if(bot_angle>=-45 and bot_angle<=45):
                return "u"
            elif(bot_angle>=45 and bot_angle<=135):
                return "r"
            elif(bot_angle>=135 or bot_angle<=-135):
                return "f"
            else:
                return "l"  
    

def angle(x1,y1,x2,y2):
    # """
    #  * Function Name: angle
    #  * Input:
    #     - x1 (float): x-coordinate of the first point.
    #     - y1 (float): y-coordinate of the first point.
    #     - x2 (float): x-coordinate of the second point.
    #     - y2 (float): y-coordinate of the second point.
    #  * Output: 
    #     - angle (float): Angle in degrees between the line connecting the two points and the x-axis.
    #       The angle is measured counterclockwise from the positive x-axis.
    #  * Logic: 
    #     This function calculates the angle between two points (x1, y1) and (x2, y2).
    #     It first calculates the differences in x and y coordinates between the two points.
    #     Then, it determines whether the x or y distance is greater, which helps determine the orientation.
    #     If the x distance is greater, it returns 90 degrees if x2 is greater than x1 (right direction),
    #     otherwise -90 degrees (left direction).
    #     If the y distance is greater, it returns 0 degrees if y2 is less than y1 (downward direction),
    #     otherwise 180 degrees (upward direction).
    #  * Example Call: 
    #     angle(0, 0, 1, 1)
        
    # * Example scenario:
    
    # Let's assume two points: (0, 0) and (1, 1).
    
    # - Since both x and y distances are equal (1 unit each), the function returns 90 degrees,
    #   indicating a right direction from the first point to the second point.
    # """
    
    x_dis=abs(x1-x2)
    y_dis=abs(y1-y2)
    if(max(x_dis,y_dis)==x_dis):
        if(x2>x1):
            return 90
        else:
            return -90
    else:
        if(y2<y1):
            return 0
        else:
            return 180

 
def find_nearest_index(target):
    # """
    #  * Function Name: find_nearest_index
    #  * Input:
    #     - target (dict): A dictionary containing the coordinates of the target point.
    #       It should have keys 'x' and 'y' representing the x-coordinate and y-coordinate respectively.
    #  * Output: 
    #     - nearest_index (int or None): The index of the nearest coordinate in the 'coordinates' list.
    #       Returns None if the 'coordinates' list is empty.
    #  * Logic: 
    #     This function finds the index of the nearest coordinate to a target point in a list of coordinates.
    #     It iterates through the 'coordinates' list and calculates the Euclidean distance between each coordinate
    #     and the target point. The index of the coordinate with the minimum distance is stored as the nearest_index.
    #     The function utilizes the math.sqrt function to calculate the square root and the ** operator for exponentiation.
    #  * Example Call: 
    #     coordinates = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 5, 'y': 6}]
    #     target = {'x': 4, 'y': 5}
    #     nearest_index = find_nearest_index(target)
    #     print(nearest_index)
        
    # Example scenario:
    
    # Let's assume a list of coordinates: [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 5, 'y': 6}].
    # And the target point is {'x': 4, 'y': 5}.
    
    # - The function calculates the distance between the target point and each coordinate.
    # - It finds that the distance from the target point to the coordinate {'x': 3, 'y': 4} is the smallest.
    # - The function returns the index of this coordinate, which is 1.
    # """
    
    min_distance = float('inf')
    nearest_index = None
    
    for i, coord in enumerate(coordinates):                                                    # Loop through coordinates
        distance = math.sqrt((coord['x'] - target['x'])**2 + (coord['y'] - target['y'])**2)    # Calculate distance between target and current coord
        if distance < min_distance:
            min_distance = distance
            nearest_index = i
    
    return nearest_index



def turning_str(l,bot_angle,ArUco_details_dict):
    # """
    #  * Function Name: turning_str
    #  * Input:
    #     - l (list): A list of integers representing the sequence of ArUco markers.
    #       Each integer corresponds to a specific ArUco marker.
    #     - bot_angle (float): Angle of the bot's orientation in degrees (-180 to 180).
    #     - ArUco_details_dict (dict): A dictionary containing details of ArUco markers.
    #       Keys are ArUco marker IDs, and values are dictionaries containing 'x' and 'y' coordinates.
    #  * Output: 
    #     - turn (str): A string representing the sequence of directions the bot should take to traverse the given path.
    #       Directions include 'f' for forward, 'b' for backward, 'l' for left, and 'r' for right.
    #  * Logic: 
    #     This function generates a string of directions that instruct the bot on how to navigate through a sequence of ArUco markers.
    #     It iterates through the list 'l', which represents the sequence of ArUco markers.
    #     For each marker, it calculates the angle between the previous and current marker using the 'angle' function,
    #     then determines the direction the bot should turn using the 'direction' function.
    #     The calculated directions are appended to the 'turn' string.
    #  * Example Call: 
    #     path = [7, 12, 18, 9, 17, 8]
    #     bot_angle = 45
    #     ArUco_details_dict = {7: {'x': 10, 'y': 20}, 12: {'x': 15, 'y': 25}, ...}
    #     directions = turning_str(path, bot_angle, ArUco_details_dict)
    #     print(directions)
        
    # Example scenario:
    
    # Let's assume a path represented by a list of ArUco markers: [7, 12, 18, 9, 17, 8].
    # The bot's initial orientation angle is 45 degrees.
    # And 'ArUco_details_dict' contains coordinates of each ArUco marker.
    
    # - The function calculates the direction from marker 7 to marker 12 based on the bot's angle.
    # - Then it calculates directions between subsequent markers using the angles calculated by the 'angle' function.
    # - The generated directions string instructs the bot on how to traverse the given path.
    # """
    
    turn=""
    flag=0
    if(l[0]=='7'):                                                                                 # Special case logic
        flag=1
    turn+=direction(cord[l[0]]['x'],cord[l[0]]['y'],cord[l[1]]['x'],cord[l[1]]['y'],bot_angle)     # Call direction function for first nodes
    for i in range(1,len(l)-1):
        if(l[i] in [17,18]):
            continue
        ang=angle(cord[l[i-1]]['x'],cord[l[i-1]]['y'],cord[l[i]]['x'],cord[l[i]]['y'])             # Calculate angle between nodes
        turn+=direction(cord[l[i]]['x'],cord[l[i]]['y'],cord[l[i+1]]['x'],cord[l[i+1]]['y'],ang)   # Call direction function
    return turn