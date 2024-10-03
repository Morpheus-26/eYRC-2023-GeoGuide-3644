#  Team Id : GG_3644
#  Author List : Mudit Agrawal
#  Filename: live_tracking_QGIS.py
#  Theme: Geo Guide (GG) Theme (eYRC 2023-24)
#  Functions: <read_csv, write_csv, tracker>
#  Global Variables: <none>



import csv

def read_csv(csv_name):
    #  """
    #  * Function Name: read_csv
    #  * Input: 
    #     - csv_name (str): The name of the CSV file to read.
    #  * Output: 
    #     - lat_lon (dict): A dictionary containing latitude and longitude information parsed from the CSV file.
    #       The keys are identifiers, and the values are lists containing latitude and longitude values.
    #  * Logic: 
    #     This function reads data from a CSV file containing latitude and longitude information.
    #     It parses the CSV file and stores the data in a dictionary where the keys are identifiers (e.g., locations) 
    #     and the values are lists containing latitude and longitude values respectively.
    #     The CSV file is assumed to have headers in the first row, where the first column represents identifiers, 
    #     the second column represents latitudes, and the third column represents longitudes.
    #  * Example Call: 
    #     lat_lon_data = read_csv("data.csv")
    
    lat_lon = {}
    with open(csv_name,'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  
        lat_lon[headers[0]]=[headers[1],headers[2]]
        for row in csv_reader:
            lat_lon[row[0]] = [row[1],row[2]]
    return lat_lon



def write_csv(loc, csv_name):
    # """
    #  * Function Name: write_csv
    #  * Input:
    #     - csv_name (str): The name of the CSV file to write.
    # 
    # - loc (list): A list containing latitude and longitude values to be written into the CSV file.
    #       The first element is latitude, and the second element is longitude.
    #  * Output: 
    #     This function does not return any value.
    #  * Logic: 
    #     This function writes latitude and longitude data to a CSV file. It takes the name of the CSV file (csv_name) 
    #     and a list containing latitude and longitude values (loc) as inputs. It then opens the specified CSV file 
    #     in write mode, writes a header row with column names 'lat' and 'lon', and writes the latitude and longitude 
    #     values from the input list into subsequent rows. Finally, it closes the CSV file.
    #  * Example Call: 
    #     write_csv("output.csv", [40.7128, -74.0060])
        
    # Example CSV file structure (output.csv):

    # | lat     | lon      |
    # |---------|----------|
    # | 40.7128 | -74.0060 |
    # """
    
    csv_file = open(csv_name, 'w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['lat', 'lon'])
    csv_writer.writerow(loc)
    csv_file.close()



def tracker(ar_id, lat_lon):
    # """
    #  * Function Name: tracker
    #  * Input:
    #     - ar_id (int or str): The identifier of the object being tracked.
    #     - lat_lon (dict): A dictionary containing latitude and longitude information for various objects.
    #       Keys are identifiers (ar_id), and values are lists containing latitude and longitude values.
    #  * Output: 
    #     This function does not return any value.
    #  * Logic: 
    #     This function tracks the location of an object specified by its identifier (ar_id) using latitude 
    #     and longitude coordinates stored in the lat_lon dictionary. It retrieves the latitude and longitude 
    #     corresponding to the provided ar_id from the lat_lon dictionary, then formats them into a list 
    #     called 'coordinate'. Finally, it calls the write_csv function to write the coordinates into 
    #     a CSV file named 'live.csv'.
    #  * Example Call: 
    #     tracker(123, {'123': [40.7128, -74.0060], '456': [34.0522, -118.2437]})
        
    # Note: 
    # The input 'ar_id' is assumed to be present in the 'lat_lon' dictionary.
    # """
    
    lat,lon = lat_lon[str(ar_id)]
    coordinate = [lat,lon]
    write_csv(coordinate, 'live.csv')  