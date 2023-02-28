# P6-AGCO
<h2>Converting of rosbags</h2>
Start by downloading the rosbag file ending with .bag (typically in the format yyyy-mm-dd-time.bag) 
<br><br>
Open a terminal and change directive to location of the .bag file (command: cd /path/to/folder_with_file). 

Run command:

```
source /opt/ros/humble/setup.bash 
```

Run one of the following commands (if --dst command is used; path should be to same destination as the file being converted)

```
# Convert "foo.bag", result will be "foo/" 
    rosbags-convert foo.bag

# Convert "bar", result will be "bar.bag"
    rosbags-convert bar

# Convert "foo.bag", save the result as "bar"
    rosbags-convert foo.bag --dst /path/to/bar

# Convert "bar", save the result as "foo.bag"
    rosbags-convert bar --dst /path/to/foo.bag
```

![image of conversion progress](.png)<br>
*Conversion may take some time - just wait*  

After conversion you should be able to run the command ***ros2 bag play*** **\<folder containing .db3 and .yaml>**

Include -l after **play** to loop file 
<br><br>
Open a new terminal. 
<br> source for ros  
```
source /opt/ros/humble/setup.bash 
```
Run command: 
```
ros2 run rqt_image_view rqt_image_view
```

![image of rqt_image_view](.png)<br>
in *rqt_image_view* choose topic in top-left corner