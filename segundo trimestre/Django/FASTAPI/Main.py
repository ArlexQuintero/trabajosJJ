from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class Producto(BaseModel):
    nombre: str
    costo: float
    categorias: str
    stock: int
    peso: float
    precio_venta: float



@app.get("/")
def read_index ():
    return "hello, esta es mi primera api"

@app.get("/productos/{id}")
def mostrar_productos (id:int):
    return {"data":id}

@app.post("/productos")
def crear_productos(producto:Producto):
    return{"message": f"El producto{producto.nombre} fue creado exitozamente", "data": producto}


@app.delete("/producto/{id}")
def eliminar_producto(id:int):
    if id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    producto_eliminado=productos_db.pop(id)
    return{
        "message": f"El producto '{producto_eliminado.nombre}' fue eliminado exitosamente.",
    }


@app.get("/productos")
def listar_productos():
    return{"data":productos_db}

productos_db={
    1:Producto(
        nombre="Laptop Lenovo",
        costo= 1200.00,
        categorias="Tecnologia",
        stock= 10,
        peso= 1.5,
        precio_venta= 1500.00
    ),
    2:Producto(
        nombre="Mause Logitec",
        costo= 50.00,
        categorias="Tecnologia",
        stock= 50,
        peso= 0.2,
        precio_venta= 80.00
    )
}