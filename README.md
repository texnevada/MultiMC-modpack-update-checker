# MultiMC-modpack-update-checker

This is a simple script that checks for updates to modpacks in MultiMC using a manifest file.
The manifest file is just a .txt file that can contain modrinth or direct mod urls.

_Note: Curseforge urls are not supported due to Cureforge adding security behind their download links. 
Making direct downloads impossible._

In your MultiMC modpack. Go to Settings and under custom commands you add the following:
```
# $INST_MC_DIR is the path to your MultiMC instance Minecraft directory.
# Make sure to put the main file inside the MultiMC instance Minecraft directory.

"$INST_MC_DIR/main.exe" --manifest "https://url-to-your-website.com/manifest.txt"
```