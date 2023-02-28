# P6-AGCO
<h2>Converting of rosbags</h2>
Start by downloading the rosbag file ending with .bag (typically in the format yyyy-mm-dd-time.bag) 
<br>
Open a terminal change directive to location of the .bag file (command: cd /path/to/folder_with_file).

# Convert "foo.bag", result will be "foo/"
rosbags-convert foo.bag

# Convert "bar", result will be "bar.bag"
rosbags-convert bar

# Convert "foo.bag", save the result as "bar"
rosbags-convert foo.bag --dst /path/to/bar

# Convert "bar", save the result as "foo.bag"
rosbags-convert bar --dst /path/to/foo.bag

