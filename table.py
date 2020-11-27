#class conexion:
#    def userSql(self):
user = input("Usuario DB:  ")

#return user

#def sqlQuery(self):
#55user = userSql
sql = "SELECT cmg.cmg_ordenes_de_trabajo.id_orden, cmg.cmg_ordenes_de_trabajo.fecha_orden, cmg.cmg_ordenes_de_trabajo.descripcion, cmg.cmg_ordenes_de_trabajo.observaciones, cmg.cmg_usuarios_sstma.nombre_usuario, cmg.cmg_usuarios_sstma.apellido_usuario, cmg.cmg_ordenes_de_trabajo.numero_radicado, cmg.cmg_prioridadtipo.nombre, cmg.cmg_ordenes_de_trabajo.estado, cmg.cmg_usuarios_sstma.id_usuario FROM cmg.cmg_ordenes_de_trabajo, cmg.cmg_usuarios_sstma, cmg.cmg_equipo_computo, cmg.cmg_prioridadtipo WHERE cmg.cmg_usuarios_sstma.id_usuario = cmg.cmg_ordenes_de_trabajo.idusuario_responsable AND cmg.cmg_equipo_computo.id_equipo_computo = cmg.cmg_usuarios_sstma.id_equipo_computo AND cmg.cmg_prioridadtipo.idprioridad = cmg.cmg_ordenes_de_trabajo.idprioridad AND cmg.cmg_ordenes_de_trabajo.idusuario_responsable = '" + user + "' AND cmg.cmg_ordenes_de_trabajo.estado = 'P' AND cmg.cmg_equipo_computo.nombre = 'PC_1'"

#return sql

#def sqlExec(self):
print(sql)

