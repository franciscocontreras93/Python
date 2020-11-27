from qgis.core import QgsVectorLayer, QgsDataSourceUri
import processing

class geoProcesos: 
    def Predio(self, tableName, cbml):

        
        #geometryCol = 'geometria'            
        exp = "'t_id' = " + str(cbml) +"'"

        uri = QgsDataSourceUri()
        uri.setConnection("181.143.104.82", "5432","prototipo", "postgres", "23826405")
        uri.setDataSource("edicion", tableName, "geometria")

        vlayer = QgsVectorLayer(uri.uri(False), tableName, "postgres")
        vlayer.setSubsetString(exp)
        vlayer.setName("Predio")

        QgsProject.instance().addMapLayer(vlayer)
        return predio('lc_terreno',1034)