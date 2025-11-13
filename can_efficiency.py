"""
Author: Robert Bruzual

Purpose: Can Storage Efficiency
Creative addition:

"""
import math

def compute_volume(radius, height):
    """Compute and return the volume of a cylinder.
    Parameters:
        radius (float): The radius of the cylinder.
        height (float): The height of the cylinder.
    Return: The volume of the cylinder.
    """
    volume = math.pi * radius**2 * height
    return volume
    
    
def compute_surface_area(radius,height):
    """Compute and return the surface area of a cylinder.
    Parameters:
        radius (float): The radius of the cylinder.
        height (float): The height of the cylinder.
    Return: The surface area of the cylinder.
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    """Compute and return the storage efficiency of a cylinder.
    Parameters:
        radius (float): The radius of the cylinder.
        height (float): The height of the cylinder.
    Return: The storage efficiency of the cylinder.
    """
    
    # Compute the volume of a can
    # by calling compute_volume()
    volume = compute_volume(radius, height)
    
    # Compute the surface area of a can
    # by calling compute_surface_area()
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    return storage_efficiency



def main():
    
    name = "#1 Picnic" 
    storage_efficiency = compute_storage_efficiency(6.83, 10.16)
    
    # Print the storage efficiency of a can
    print(f"{name} {storage_efficiency:.2f}")
    # Storage efficiency for can 2
    name = "#1 Tall"
    storage_efficiency = compute_storage_efficiency(7.78, 11.91)
    print(f"{name} {storage_efficiency:.2f}")
# Start this program by calling the main function.
main()   