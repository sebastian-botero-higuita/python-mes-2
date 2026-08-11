# app/routers/empleados.py
from app.database import EMPLEADOS
from app.schemas import EmpleadoActualizar, EmpleadoCrear, EmpleadoRespuesta
from fastapi import APIRouter, HTTPException, status

# Inicializamos el APIRouter con prefijo centralizado y etiqueta para Swagger UI
router = APIRouter(prefix="/empleados", tags=["Empleados"])


@router.get("", response_model=list[EmpleadoRespuesta])
def obtener_empleados(cargo: str | None = None):
    if cargo:
        return [
            emp
            for emp in EMPLEADOS
            if emp["cargo"].lower() == cargo.lower()
        ]
    return EMPLEADOS


@router.get("/{empleado_id}", response_model=EmpleadoRespuesta)
def obtener_empleado_por_id(empleado_id: int):
    for emp in EMPLEADOS:
        if emp["id"] == empleado_id:
            return emp

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Empleado con ID {empleado_id} no fue encontrado",
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=EmpleadoRespuesta,
)
def crear_empleado(nuevo_empleado: EmpleadoCrear):
    empleado_dict = nuevo_empleado.model_dump()
    EMPLEADOS.append(empleado_dict)
    return empleado_dict


@router.put("/{empleado_id}", response_model=EmpleadoRespuesta)
def actualizar_empleado(
    empleado_id: int, datos_actualizados: EmpleadoActualizar
):
    for emp in EMPLEADOS:
        if emp["id"] == empleado_id:
            datos_dict = datos_actualizados.model_dump()
            emp["nombre"] = datos_dict["nombre"]
            emp["cargo"] = datos_dict["cargo"]
            emp["salario"] = datos_dict["salario"]
            return emp

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No se puede actualizar. Empleado con ID {empleado_id} no fue encontrado",
    )


@router.delete("/{empleado_id}")
def eliminar_empleado(empleado_id: int):
    for index, emp in enumerate(EMPLEADOS):
        if emp["id"] == empleado_id:
            empleado_eliminado = EMPLEADOS.pop(index)
            return {
                "mensaje": f"Empleado con ID {empleado_id} eliminado con éxito",
                "empleado_eliminado": empleado_eliminado["nombre"],
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No se puede eliminar. Empleado con ID {empleado_id} no fue encontrado",
    )