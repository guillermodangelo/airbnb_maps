import os
import time

years = list(range(2010, 2024))
base_path = "C:/Users/59898/Desktop/airbnb_maps/maps_buenos_aires/"
layer = iface.activeLayer()

for year in years: 
    layer.setSubsetString(f"""year = {year}""")
    iface.mapCanvas().refreshAllLayers()
    time.sleep(2)

    # instantiates the print composer
    projectLayoutManager = QgsProject.instance().layoutManager()
    layout = projectLayoutManager.layoutByName('map')
    layout.refresh()

    # exports
    path = os.path.join(base_path, f'map_{year}.jpg')
    print(f'Exporting map to {path}')
    exporter = QgsLayoutExporter(layout)
    exporter.exportToImage(path, QgsLayoutExporter.ImageExportSettings())
    time.sleep(3)