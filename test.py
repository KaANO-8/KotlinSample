import xml.etree.ElementTree as ET
from xml.dom import minidom


tree = ET.parse('./AndroidStudioProjects/KotlinSample/app/src/main/res/layout/activity_main.xml')
root = tree.getroot()


ImageView_Layout = ET.Element("LinearLayout", {"android:layout_width": "match_parent",
                            "android:layout_height": "wrap_content",
                            "android:background": "@drawable/border",
                            "android:layout_margin":"10dp",
                            "android:orientation":"vertical"})
                            
image = ET.Element("ImageView", {"android:layout_width": "match_parent",
                            "android:layout_height": "220dp",
                            "android:src": "@drawable/digital",
                            "android:padding":"10dp"})
                                                        
line = ET.Element("LinearLayout", {"android:layout_width": "match_parent",
                            "android:layout_height": "1dp",
                            "android:background": "#000"})
                               
caption = ET.Element("TextView", {"android:layout_width": "match_parent",
                            "android:layout_height": "wrap_content",
                            "android:text": "@string/image_caption",
                            "android:textColor":"#000",
                            "android:textSize":"20sp",
                            "android:gravity":"center",
                            "android:padding":"10dp"})

ImageView_Layout.append(image)
ImageView_Layout.append(line)
ImageView_Layout.append(caption)


TextView_Layout = ET.Element("LinearLayout", {"android:layout_width": "match_parent",
                            "android:layout_height": "wrap_content",
                            "android:paddingLeft": "20dp",
                            "android:paddingRight":"20dp",
                            "android:orientation":"vertical"})

title = ET.Element("TextView", {"android:layout_width": "match_parent",
                            "android:layout_height": "wrap_content",
                            "android:text": "@string/tv_title",
                            "android:textSize":"25sp",
                            "android:textColor":"#000"})

author = ET.Element("TextView", {"android:layout_width": "match_parent",
                            "android:layout_height": "wrap_content",
                            "android:text": "@string/author",
                            "android:textSize":"18sp"})

content = ET.Element("TextView", {"android:layout_width": "match_parent",
                            "android:layout_height": "wrap_content",
                            "android:text": "@string/content",
                            "android:textSize":"18sp",
                            "android:layout_marginTop":"5dp"})

# appending each data to textView
TextView_Layout.append(title)
TextView_Layout.append(author)
TextView_Layout.append(content)


out = ET.tostring(ImageView_Layout)
print(out)
#dom = minidom.parseString(out)
#print(dom.toprettyxml())
'''
    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/tv1"
        android:textSize="25sp"
        android:gravity="center" />
        '''