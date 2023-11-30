# Pyramid pattern
def pyramid(n):
    """
    Function to create a pyramid pattern.

    Args:
        n (int): Number of rows in the pyramid.

    Returns:
        None
    """
    for i in range(n):
        # Print spaces before the stars
        print(" " * (n - i - 1), end="")
        
        # Print stars
        print("*" * (2 * i + 1))

# Half pyramid pattern
def half_pyramid(n):
    """
    Function to create a half pyramid pattern.

    Args:
        n (int): Number of rows in the pyramid.

    Returns:
        None
    """
    for i in range(n):
        # Print stars
        print("*" * (i + 1))

# Backwards pyramid pattern
def backwards_pyramid(n):
    """
    Function to create a backwards pyramid pattern.

    Args:
        n (int): Number of rows in the pyramid.

    Returns:
        None
    """
    for i in range(n, 0, -1):
        # Print spaces before the stars
        print(" " * (n - i), end="")
        
        # Print stars
        print("*" * (2 * i - 1))

# All types of pyramids
def all_pyramids(n):
    """
    Function to create all types of pyramids.

    Args:
        n (int): Number of rows in the pyramid.

    Returns:
        None
    """
    print("Pyramid pattern:")
    pyramid(n)
    
    print("\nHalf pyramid pattern:")
    half_pyramid(n)
    
    print("\nBackwards pyramid pattern:")
    backwards_pyramid(n)

# Test the functions
n = 5
all_pyramids(n)
