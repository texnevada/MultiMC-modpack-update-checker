# MultiMC-modpack-update-checker

This is a simple script that checks for updates to modpacks in MultiMC using a manifest file.
The manifest file is just a .txt file that can contain modrinth or direct mod urls.

_Note: Curseforge urls are not supported due to Cureforge adding security behind their download links. 
Making direct downloads impossible._

In your MultiMC modpack. Go to Settings and under custom commands you add the following:
```text
# $INST_MC_DIR is the path to your MultiMC instance Minecraft directory.
# Make sure to put the main file inside the MultiMC instance Minecraft directory.

"$INST_MC_DIR/main.exe" --manifest "https://url-to-your-website.com/manifest.txt"
```

The manifest file supports # comments and empty lines. Meaning you can add some personal 
structure to your manifest file.

The manifest file can look like this:
```text
https://cdn.modrinth.com/data/gvQqBUqZ/versions/m6sVgAi6/lithium-fabric-mc1.19.2-0.11.1.jar
https://cdn.modrinth.com/data/fQEb0iXm/versions/0.2.1/krypton-0.2.1.jar
https://cdn.modrinth.com/data/qQyHxfxd/versions/YuX53PIA/NoChatReports-FABRIC-1.19.2-v1.13.12.jar
```

or like this:
```text
#####################################################################################################
#                                         Server side mods                                          #
#####################################################################################################

# View distance fix. Server fakes the view distance. Not needed on client side
https://cdn.modrinth.com/data/nxrXbh5K/versions/6YGGQq3R/viewdistancefix-1.19.2-1.0.0.jar

# Spark. Server side analytics mod but useful on client side to provide server with more information
https://cdn.modrinth.com/data/l6YH9Als/versions/XhFbpH8f/spark-1.10.37-fabric.jar
```