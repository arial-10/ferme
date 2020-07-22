-- --GRUPOS
-- INSERT INTO AUTH_GROUP(NAME, ID) VALUES('vendedor', 1);
-- INSERT INTO AUTH_GROUP(NAME, ID) VALUES('empleado', 2);
-- INSERT INTO AUTH_GROUP(NAME, ID) VALUES('cliente', 3);
-- INSERT INTO AUTH_GROUP(NAME, ID) VALUES('administrador', 4);

-- -- EMPLEADO
-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(5, 'fgomez','fgomez@gmail.com','12345', 0, 0, 1, TO_DATE('01/01/2020', 'DD/MM/YYYY'));
-- INSERT INTO empleado
-- VALUES (1, '18454865-5', 'Fernando Agustin', 'Gomez', 'Valenzuela', TO_DATE('10/05/1993', 'DD/MM/YYYY'), 'M', 'fgomez@gmail.com', 956213148, 'fgomez', '12345', 'EMP101', 'CASA MATRIZ', TO_DATE('01/01/2020', 'DD/MM/YYYY'), 'Despacho', 5);

-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(6, 'cencina','clara85@gmail.com','4561', 0, 0, 1, TO_DATE('08/06/2015', 'DD/MM/YYYY'));
-- INSERT INTO empleado
-- VALUES (2, '15451231-8', 'Clara Luisa', 'Encina', 'Carrasco', TO_DATE('05/08/1985', 'DD/MM/YYYY'), 'F', 'clara85@gmail.com', 936125489, 'cencina', '4561', 'EMP102', 'CASA MATRIZ', TO_DATE('08/06/2015', 'DD/MM/YYYY'), 'Ventas',6);

-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(7, 'jgonzalez','juantonio12@gmail.com','8888', 0, 0, 1, TO_DATE('15/09/2019', 'DD/MM/YYYY'));
-- INSERT INTO empleado
-- VALUES (3, '16845123-5', 'Juan Antonio', 'Gonzalez', 'Soto', TO_DATE('22/08/1988', 'DD/MM/YYYY'), 'M', 'juantonio12@gmail.com', 965312487, 'jgonzalez', '8888', 'EMP103', 'CASA MATRIZ', TO_DATE('15/09/2019', 'DD/MM/YYYY'), 'Recepcion',7);

-- --ASOCIAMOS LOS EMPELADOS A SUS GRUPOS
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(5,2);
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(6,2);
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(7,2);

-- -- CLIENTE
-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(8, 'david.cop','davidtruquito@gmail.com','12345', 0, 0, 1, TO_DATE('21/07/2020', 'DD/MM/YYYY'));
-- INSERT INTO cliente(usuario_id, run, nombres, appaterno, apmaterno, fecha_nacimiento, genero, email, telefono, nombre_usuario, contrasena, direccion, user_id)
-- VALUES (1, '14098120-1', 'David Anthony', 'Copperfield', 'Johnson', TO_DATE('18/11/1978', 'DD/MM/YYYY'), 'M', 'davidtruquito@gmail.com', 978432164, 'david.cop', '12345', 'Los Alerces 20, Peñaflor', 8);

-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(9, 'ariel1007','ariboni@gmail.com','1007', 0, 0, 1, TO_DATE('21/07/2020', 'DD/MM/YYYY'));
-- INSERT INTO cliente(usuario_id, run, nombres, appaterno, apmaterno, fecha_nacimiento, genero, email, telefono, nombre_usuario, contrasena, direccion, user_id)
-- VALUES (2, '18347172-5', 'Ariel Bonifacio', 'Gonzalez', 'Torres', TO_DATE('10/03/1993', 'DD/MM/YYYY'), 'M', 'ariboni@gmail.com', 965448124, 'ariel1007', '1007', 'Los Puelches 928, Peñaflor',9);

-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(10, 'cinthi10','dark1544@gmail.com','4800021', 0, 0, 1, TO_DATE('21/07/2020', 'DD/MM/YYYY'));
-- INSERT INTO cliente(usuario_id, run, nombres, appaterno, apmaterno, fecha_nacimiento, genero, email, telefono, nombre_usuario, contrasena, direccion, user_id)
-- VALUES (3, '17512453-7', 'Cinthia Andrea', 'Gomez', 'Espinoza', TO_DATE('22/02/1988', 'DD/MM/YYYY'), 'F', 'dark1544@gmail.com', 956412316, 'cinthi10', '4800021', 'Neptuno 90, Talagante', 10);

-- --ASOCIAMOS LOS CLIENTES A SUS GRUPOS
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(8,3);
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(9,3);
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(10,3);

-- -- VENDEDOR
-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(4, 'jsanhueza','joje876@gmail.com','jusi21', 0, 0, 1, TO_DATE('15/03/2019', 'DD/MM/YYYY'));
-- INSERT INTO vendedor 
-- VALUES (4, '17556484-6', 'Jose Antonio', 'Sanhueza', 'Peña', TO_DATE('26/07/1989', 'DD/MM/YYYY'), 'M', 'joje876@gmail.com', 973647321, 'jsanhueza', 'jusi21', 'VEN101', 'CASA MATRIZ', TO_DATE('15/03/2019', 'DD/MM/YYYY'), 4);

-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(2, 'jromero','josefa1111@gmail.com','a1548', 0, 0, 1, TO_DATE('08/02/2005', 'DD/MM/YYYY'));
-- INSERT INTO vendedor VALUES (2, '14320125-2', 'Josefa Belen', 'Romero', 'Veliz', TO_DATE('30/04/1980', 'DD/MM/YYYY'), 'F', 'josefa1111@gmail.com', 988974521, 'jromero', 'a1548', 'VEN102', 'CASA MATRIZ', TO_DATE('08/02/2005', 'DD/MM/YYYY'),2);

-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(3, 'gquintanilla','gonzalohet6@gmail.com','gonzi12', 0, 0, 1, TO_DATE('02/04/2019', 'DD/MM/YYYY'));
-- INSERT INTO vendedor VALUES (3, '17556484-6', 'Gonzalo Ivan', 'Quintanilla', 'Ramos', TO_DATE('15/06/1992', 'DD/MM/YYYY'), 'M', 'gonzalohet6@gmail.com', 988745136, 'gquintanilla', 'gonzi12', 'VEN103', 'CASA MATRIZ', TO_DATE('02/04/2019', 'DD/MM/YYYY'),3);

-- -- TIENDA VIRTUAL
-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(1, 'tienda_virtual','tienda@ferme.cl','fermetienda2020', 0, 0, 1, TO_DATE('01/03/2020', 'DD/MM/YYYY'));
-- INSERT INTO vendedor 
-- VALUES (1, '13371337-1', 'FERME', 'FERME', 'FERME', TO_DATE('01/03/2020', 'DD/MM/YYYY'), 'N', 'tienda@ferme.cl', 6006003279, 'tienda_virtual', 'fermetienda2020', 'VEN000', 'CASA MATRIZ', TO_DATE('01/03/2020', 'DD/MM/YYYY'),1);

-- --ASOCIAMOS LOS VENDEDORES A SUS GRUPOS
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(1,1);
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(2,1);
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(3,1);
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(4,1);

-- -- ADMINISTRADOR
-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(11, 'gfigueroa','gustavock1@gmail.com','gfigueroa', 0, 0, 1, TO_DATE('01/03/2020', 'DD/MM/YYYY'));
-- INSERT INTO administrador VALUES (1, '16489546-K', 'Gustavo Andres', 'Figueroa', 'Romero', TO_DATE('20/10/1987', 'DD/MM/YYYY'), 'M', 'gustavock1@gmail.com', 945461234, 'gfigueroa', 'gas23123', 'ADM101', 11);

-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(12, 'fperez','fran.jav@gmail.com','fperez', 0, 0, 1, TO_DATE('01/03/2020', 'DD/MM/YYYY'));
-- INSERT INTO administrador VALUES (2, '17894561-5', 'Francisca Javiera', 'Perez', 'Bustamante', TO_DATE('18/12/1990', 'DD/MM/YYYY'), 'F', 'fran.jav@gmail.com', 9458749965, 'fperez', '12548', 'ADM102', 12);

-- INSERT INTO AUTH_USER(ID, USERNAME, email, PASSWORD, IS_SUPERUSER, IS_STAFF, IS_ACTIVE, DATE_JOINED)
-- VALUES(13, 'gcampos','gloria.campos@gmail.com','gcampos', 0, 0, 1, TO_DATE('01/03/2020', 'DD/MM/YYYY'));
-- INSERT INTO administrador VALUES (3, '12356994-4', 'Gloria Esperanza', 'Campos', 'Videla', TO_DATE('02/03/1970', 'DD/MM/YYYY'), 'F', 'gloria.campos@gmail.com', 989458754, 'gcampos', '001215', 'ADM103', 13);

-- --ASOCIAMOS LOS ADMINISTRADORES A SUS GRUPOS
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(11,4);
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(12,4);
-- INSERT INTO AUTH_USER_GROUPS(USER_ID, GROUP_ID)
-- VALUES(13,4);

--MARCA
INSERT INTO marca VALUES (101, 'Redline');
INSERT INTO marca VALUES (102, 'Holztek');
INSERT INTO marca VALUES (103, 'Bauker');
INSERT INTO marca VALUES (104, 'Thomas Flinn');
INSERT INTO marca VALUES (105, 'Ceresita');

--CATEGORIA
INSERT INTO categoria VALUES (101, 'Construcción');
INSERT INTO categoria VALUES (102, 'Herramientas');
INSERT INTO categoria VALUES (103, 'Maquinaria');
INSERT INTO categoria VALUES (104, 'Piso y Pared');
INSERT INTO categoria VALUES (105, 'Baño y Cocina');
INSERT INTO categoria VALUES (106, 'Iluminación y Electricidad');
INSERT INTO categoria VALUES (107, 'Automóviles');

--PRODUCTO
INSERT INTO producto VALUES ('2984646413121', '2998814752605', 'Martillo carpintero', NULL, 'Martillo carpintero 20 Oz acero', 100, 50, 'S', 5000, 4790, 'img/producto/2984646413121.jpg', 101);
INSERT INTO producto VALUES ('2984646234234', '2998814755042', 'Piso Flotante', 'Nogal', 'Piso flotante 138x19,3 cm 2,92 m2', 599, 250, 'S', 3890, 2690, 'img/producto/2984646234234.jpg', 102);
INSERT INTO producto VALUES ('2984646645334', '2998814750907', 'Sierra circular electrica', NULL, 'Sierra circular electrica 7 1/4 1800W', 960, 350, 'S', 54980, 39890, 'img/producto/2984646645334.jpg', 103);
INSERT INTO producto VALUES ('3489451234542', '7845513451543', 'Serrucho de ebanista 12" TPI rip', NULL, 'Sierra de Costilla Cola de Milano. Tipo de Corte: Ripcut (Longitudinal a la Veta). Las Sierras de Mano Thomas Flinn están hechas con acero al carbono de resorte de la más alta calidad y están rectificadas con una inclinación hacia atrás y una línea recta de dientes. Espesor del corte: 1.05mm. Profundidad de Corte: 75mm', 10, 10, 'S', 49990, 34490, 'img/producto/3489451234542.jpg', 104);
INSERT INTO producto VALUES ('3026487542121', '3978451615454', 'Esmalte Sintetico Cereluxe Aquatech Semibrillo', 'Café moro', 'Formulado con resinas alquídicas soluble en agua. Ideal para maderas y metales.', 2, 20, 'S', 6990, 6490, 'img/producto/3026487542121.jpg', 105);
INSERT INTO producto VALUES ('5649754621448', '7894644665474', 'Protector de madera satinado 1/4 gl', 'Encina', 'El Protector de madera Cerestain Ceresita es un producto de pintura y accesorios que ha sido desarrollado especialmente para la protección de maderas que se usan en ambientes exteriores. Se trata de una sustancia con un alto poder de penetración que es muy resistente a los rayos UV.', 0, 20, 'N', 8990, 7990, 'img/producto/5649754621448.jpg', 105);

--CATEGORIA PRODUCTO
INSERT INTO categoriaproducto VALUES (1, 101, '2984646413121');
INSERT INTO categoriaproducto VALUES (2, 102, '2984646413121');
INSERT INTO categoriaproducto VALUES (3, 104, '2984646234234');
INSERT INTO categoriaproducto VALUES (4, 103, '2984646645334');
INSERT INTO categoriaproducto VALUES (5, 101, '3489451234542');
INSERT INTO categoriaproducto VALUES (6, 102, '3489451234542');
INSERT INTO categoriaproducto VALUES (7, 101, '3026487542121');
INSERT INTO categoriaproducto VALUES (8, 101, '5649754621448');

-- -- DESPACHO DOMICILIO
-- INSERT INTO despachodomicilio VALUES (1, TO_DATE('10/05/2020', 'DD/MM/YYYY'), '14.098.120-1', 'ENTREGADO', 'Los Alerces 20', 978432164, 'Peñaflor', NULL, 101);
-- INSERT INTO despachodomicilio VALUES (2, TO_DATE('12/05/2020', 'DD/MM/YYYY'), '14.098.120-1', 'ENTREGADO', 'Los Alerces 20', 978432164, 'Peñaflor', NULL, 102);
-- INSERT INTO despachodomicilio VALUES (3, TO_DATE('28/04/2020', 'DD/MM/YYYY'), '18.347.172-5', 'ENTREGADO', 'Los Puelches 928', 965448124, 'Peñaflor', NULL, 103);

-- ACTIVIDAD
-- ESTO NO SE PUEDE IMPLEMENTAR DE MOMENTO: LA CLAVE FORANEA PERTENECE A UNA CLASE INTERNA DE DJANGO QUE NO ES USADA
-- INSERT INTO actividad VALUES (1, TO_DATE('10/05/2020 14:30', 'DD/MM/YYYY HH24:MI'), 1);
-- INSERT INTO actividad VALUES (2, TO_DATE('10/05/2020 16:15', 'DD/MM/YYYY HH24:MI'), 3);
-- INSERT INTO actividad VALUES (3, TO_DATE('11/05/2020 18:33', 'DD/MM/YYYY HH24:MI'), 2);

-- BOLETA, FACTURA Y NOTA DE CREDITO
-- INSERT INTO factura VALUES (1, 'CASA MATRIZ', 'CALLE FALSA 123', 'MAIPU', TO_DATE('05/05/2020', 'DD/MM/YYYY'), 0, 'EFECTIVO', '5555888-1', 3400, 101, 'VALIDA');
-- INSERT INTO boleta VALUES(1, 'CASA MATRIZ', 'Los Puelches 928, Peñaflor', 'PEÑAFLOR', TO_DATE('05/05/2020', 'DD/MM/YYYY'), 0, 'EFECTIVO', 'VALIDA', 102, '14.098.120-1');
-- INSERT INTO boleta VALUES(2, 'CASA MATRIZ', 'Los Puelches 928, Peñaflor', 'PEÑAFLOR', TO_DATE('01/05/2020', 'DD/MM/YYYY'), 0, 'EFECTIVO', 'ANULADA', 103, '14.098.120-1');
-- INSERT INTO notacredito VALUES(1, 'CASA MATRIZ', 'Los Puelches 928, Peñaflor', 'PEÑAFLOR', TO_DATE('01/05/2020', 'DD/MM/YYYY'), 0, 'EFECTIVO', TO_DATE('02/05/2020', 'DD/MM/YYYY'), 'B2', 'SIERRA EN MAL ESTADO', 103, 1 , 'VALIDA');

-- PROVEEDOR
INSERT INTO proveedor VALUES(111, 'RON SWANSON EIRL', 'CARPINTERIA', 'Malloquito 2354', 'ronswanson@parks.cl', '5695559292');
INSERT INTO proveedor VALUES(222, 'RON BURGUNDY SPA', 'CONSTRUCCION', 'El Comendador 1041', 'ronburgundy@KVWN.cl', '5692345872');
INSERT INTO proveedor VALUES(333, 'BOB THE BUILDER SPA', 'CONSTRUCCION', 'Doce de Septiempre 3148', 'bob@yeswecan.cl', '5695874926');

-- ORDEN DE COMPRA
INSERT INTO ordendecompra VALUES(011, TO_DATE('01/MAY/20', 'DD/MM/YYY'), 'RECIBIDA', 333);
INSERT INTO ordendecompra VALUES(022, TO_DATE('05/04/2020', 'DD/MM/YYYY'), 'RECIBIDA', 222);
INSERT INTO ordendecompra VALUES(033, TO_DATE('21/05/2020', 'DD/MM/YYYY'), 'PENDIENTE', 111);

-- PRODUCTO_OC
INSERT INTO productooc (id, orden_de_compra_id, producto_id, cantidad) VALUES(1, 011, '2984646413121', 200);
INSERT INTO productooc (id, orden_de_compra_id, producto_id, cantidad) VALUES(3, 022, '2984646645334', 20);
INSERT INTO productooc (id, orden_de_compra_id, producto_id, cantidad) VALUES(2, 033, '2984646234234', 300);

-- PROVEEDOR PRODUCTO
INSERT INTO proveedorproducto VALUES (1, '2984646413121', 111);
INSERT INTO proveedorproducto VALUES (2, '3489451234542', 111);
INSERT INTO proveedorproducto VALUES (3, '3026487542121', 222);
INSERT INTO proveedorproducto VALUES (4, '5649754621448', 222);
INSERT INTO proveedorproducto VALUES (5, '2984646234234', 333);
INSERT INTO proveedorproducto VALUES (6, '2984646645334', 333);

