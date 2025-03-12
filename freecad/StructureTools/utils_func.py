import FreeCAD, Part
from functools import lru_cache
from.config import BASE_ARROWS_DIM, AZUL, VERMELHO, VERDE, FORCE_SCALE


def str_dir_to_vet(direction:str):
        y_vet = FreeCAD.Vector(0,1,0)
        x_vet = FreeCAD.Vector(1,0,0)
        z_vet = FreeCAD.Vector(0,0,1)
        vet_map = {
            '+X':x_vet,
            '-X':-x_vet,
            '+Y':y_vet,
            '-Y':-y_vet,
            '+Z':z_vet,
            '-Z':z_vet,
            }
        return vet_map.get(direction)

def rotate_to_direction(direction:str, obj):
    """
    Rotaciona um objeto fornecido na direção desejada.
    Direções Suportadas:
    '+X','-X','+Y','-Y','+Z','-Z'
    """
    null_vet = FreeCAD.Vector(0,0,0)
    y_vet = str_dir_to_vet('+Y')
    x_vet = str_dir_to_vet('+X')
    rotate_map = {
        '+X':(null_vet,y_vet, -90),
        '-X':(null_vet,y_vet, 90),
        '+Y':(null_vet,x_vet, 90),
        '-Y':(null_vet,x_vet, -90),
        '+Z':(null_vet,x_vet, 180),
        '-Z':(null_vet,x_vet, 0),
        }
    if direction not in rotate_map.keys():
        print("Invalid Direction!")
        return
    obj.rotate(*rotate_map.get(direction))

@lru_cache(maxsize=2)
def make_arrow_point(
    base_radius=BASE_ARROWS_DIM.get('base_radius_cone'), 
    height=BASE_ARROWS_DIM.get('height_cone'), 
    scale = 1):
    """Cria um cone de acordo com as medidas enviadas.
    Possue um cache para as duas primeiras chamadas.
    base_radius - raio base em mm
    heights - height em mm
    scala -  fator de escala
    """
    return Part.makeCone(0 ,base_radius * scale , height * scale )


def make_arrow(
        height_arrow, 
        radius_cylinder = BASE_ARROWS_DIM.get('radius_cylinder'), 
        base_radius_cone=BASE_ARROWS_DIM.get('base_radius_cone'), 
        height_cone=BASE_ARROWS_DIM.get('height_cone'), 
        scale=1):
    """Cria uma seta de acordo com as medidas enviadas.
    Caso a seta tenha tamanho menor (em modulo) que a altura da seta, a função retorna None
    """
    height_cylinder = abs(height_arrow/FORCE_SCALE)
    if height_cone > height_cylinder:
        return
    cone = make_arrow_point(base_radius_cone,height_cone,scale)
    height_cylinder = height_cylinder - height_cone
    cylinder = Part.makeCylinder(radius_cylinder * scale , height_cylinder * scale )        
    cylinder.translate(FreeCAD.Vector(0,0, height_cone * scale ))
    shape = Part.makeCompound([cone, cylinder])
    if height_arrow < 0:
        rotate_to_direction('+Z',shape)
    return shape

def make_momentum_arrow(
        height_arrow, 
        radius_cylinder = BASE_ARROWS_DIM.get('radius_cylinder'), 
        base_radius_cone=BASE_ARROWS_DIM.get('base_radius_cone'), 
        height_cone=BASE_ARROWS_DIM.get('height_cone'), 
        scale=1):
    height_cylinder = abs(height_arrow/FORCE_SCALE)
    if (2*height_cone) > height_cylinder:
        return
    cone = make_arrow_point(base_radius_cone, height_cone, scale)
    cone2 = cone.copy()
    cone2.translate(FreeCAD.Vector(0,0, height_cone * scale ))
    height_cylinder = height_cylinder - 2 * height_cone
    cylinder = Part.makeCylinder(radius_cylinder * scale , abs(height_cylinder) * scale )        
    cylinder.translate(FreeCAD.Vector(0,0, height_cone * 2 * scale ))
    shape = Part.makeCompound([cone,cone2, cylinder])
    if height_arrow < 0:
        rotate_to_direction('+Z',shape)
    return shape

def set_obj_appear(obj, option=0):
    """
    obj - > shape freecad
    option - > int
    0 to blue
    1 to red
    2 to gree
    """
    if option == 0:
        material = AZUL
    if option == 1:
        material = VERMELHO
    if option == 2:
        material = VERDE
        
    obj.ViewObject.ShapeAppearance = (
                FreeCAD.Material(**material))
