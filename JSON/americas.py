import pygal

wm = pygal.Worldmap()
wm.title = 'Notrh,Central,and South America'

wm.add('North America',['ca','mx','us'])
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America',['ar','bo','br','cl','co','ec','gt','gy','pe','py','sr','uy','ve'])
wm.render_to_file('americas.svg')