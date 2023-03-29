# MinecraftAIAntiCheatPOC
Proof of concept for a nueral network based cheat detection system for movment based cheats in videogames. 
# Basic premises: 
  1. Collect large amounts of movement data of players that are not cheating in your game of choice
  2. Collect movement data of players that are cheating in your game of choice
  3. Train the network to know what cheating movement "looks" like
  4. Decide the threshold for detection/ number of detections required to notify staff or auto-ban the player
# Video
Things shown in video 
  1. Record player XYZ coords and their velocity while they are walking then save and rename the file
  2. Record player XYZ coords and their velocity while they are "flyhacking" (in this case just creative) then save and rename the file
  3. Moved files to neural network project folder
  4. Run prediction whether the data is walking or flying. 

  Notes: In this case the player data was gained by ripping it right out of my system memory but you could also get this data from a minecraft server logging plugin. The   detection can also be done in real time.
