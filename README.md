# Haar-Face-Extractor
A python script that extracts faces from images. Uses Haar Cascade.
<br><br>
Requirements:<br>
- python<br>
- opencv<br>

Sample input:<br>
<img src="./in/Morgan Freeman/16.jpg" width=200 height=200>
<img src="./in/Morgan Freeman/12.jpg" wdith = 200 height=200>
<br>Sample output:<br>
<img src="./out/Morgan Freeman/16.jpg_index-0.png" width=200 height=200>
<img src="./out/Morgan Freeman/12.jpg_index-0.png" width=200 height=200>

<br>
#Note:<br>
From my sample data of 1,847 images, it extracted a total of 1,570 images, only 886 of which had actual faces.<br>
Busy images might extract undesirable parts, such as background, objects and body parts that is not the whole face.<br>
Faces might not be extracted if the image is rotated, or the face is not facing directly, etc.
