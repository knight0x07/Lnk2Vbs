# Lnk2Vbs

A Python script that embeds Target VBS into LNK and when executed runs the VBS script from within.

# Screenshots

Execution of Script:

![Screenshot_2](https://user-images.githubusercontent.com/60843949/199551813-95de2898-e762-455f-9f4d-cd3a78ef0037.png)

Here we provide all the required arguments to the .LNK File. 
Along with this we also provide the name of the Target VBS script (should be present in the same directory as the script) to be embedded inside the LNK file.

Once the execution of the script is completed, it generates the LNK File in the same directory with the embedded VBS script as shown below

![3](https://user-images.githubusercontent.com/60843949/199552887-2fe8d3a4-263d-4198-b07e-761d6222338c.PNG)

And then when we execute the final LNK file which in turn runs the embedded VBS Script (embed.vbs) from within -> which further spawns the favourite "calc.exe" :

![Captur2](https://user-images.githubusercontent.com/60843949/199555104-e0fc4cb3-c5f2-4ed4-88ba-12845833f07f.PNG)

# Note

For educational purposes only.
