import os
android='./proj.android/res/'
ios='./proj.ios_mac/ios/'
ios_outs=['29','40','50','57','58','72','76','80','100','114','120','144','152']
android_outs=['32','48','72','128']
android_path=['drawable-ldpi','drawable-mdpi','drawable-hdpi','drawable-xhdpi']
ios_start_resolutions=['320x480','640x960','640x1136']
start_names = ['Default.png','Default@2x.png','Default-568h@2x.png']
print 'ios icon...'
print ios_outs
for resolution in ios_outs:
    name=ios + 'Icon-'+resolution+'.png'
    print name
    os.popen('convert -resize '+resolution+'x'+resolution+'!' +' icon512x512.png '+ name )
print 'ios Launch images...'
for start_name,resolution in zip(start_names,ios_start_resolutions):
    name = ios+start_name
    os.popen('convert -resize '+ resolution+'! '+'binding.png '+name)
print 'android icon...'
for path,resolution in zip(android_path,android_outs):
    name=android+path+'/icon.png'
    print name
    os.popen('convert -resize ' + resolution +'x'+ resolution+'!'+' icon512x512.png ' +name )
