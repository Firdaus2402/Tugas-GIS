import mapnik
m = mapnik.Map(3840,2160)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#C5E384')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Firdaus2',s)
ds = mapnik.Shapefile(file="countries/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Firdaus2')
m.layers.append(layer)


# MAP 1 CHINA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#7FFF00')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Firdaus',s)
ds = mapnik.Shapefile(file="map china/china.shp")
layer = mapnik.Layer('negarachina')
layer.datasource = ds
layer.styles.append('Firdaus')
m.layers.append(layer)
# BATAS AKHIR MAP 1 DUNIA

# MAP 2 India
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FFF00F')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Firdaus2',s)
ds = mapnik.Shapefile(file="map india/India.shp")
layer = mapnik.Layer('NegaraIndia')
layer.datasource = ds
layer.styles.append('Firdaus2')
m.layers.append(layer)
# BATAS AKHIR MAP 2 India

# MAP 3 Indonesia
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#00FFFF')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Firdaus3',s)
ds = mapnik.Shapefile(file="map indonesia/indonesia.shp")
layer = mapnik.Layer('negaraindonesia')
layer.datasource = ds
layer.styles.append('Firdaus3')
m.layers.append(layer)
# BATAS MAP 3 Indonesia

# MAP 4 Somalia
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FFF000')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Firdaus4',s)
ds = mapnik.Shapefile(file="map somalia/somalia.shp")
layer = mapnik.Layer('NegaraSomalia')
layer.datasource = ds
layer.styles.append('Firdaus4')
m.layers.append(layer)
# BATAS MAP 4 Somalia

# MAP 5 Turkey
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FF00F0')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Firdaus5',s)
ds = mapnik.Shapefile(file="map turkey/Turkey.shp")
layer = mapnik.Layer('negaraTurkey')
layer.datasource = ds
layer.styles.append('Firdaus5')
m.layers.append(layer)
# BATAS MAP 5 Turkey

m.zoom_all()
mapnik.render_to_file(m,'world.jpeg','jpeg')
print "rendered image to 'world.jpeg'"
