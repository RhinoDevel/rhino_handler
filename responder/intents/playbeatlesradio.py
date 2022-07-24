
# Marcel Timm, RhinoDevel, 2022jul23

from audio import player

LOCATION = 'https://strw1.openstream.co/981?aw_0_1st.collectionid%3D6906%26stationId%3D6906%26publisherId%3D1005%26k%3D1657900117%26aw_0_azn.pcountry%3D%5B%22US%22%5D%26aw_0_azn.planguage%3D%5B%22en%22%5D%26aw_0_azn.p'

def exec(params):
    player.play(LOCATION)
    return ''
