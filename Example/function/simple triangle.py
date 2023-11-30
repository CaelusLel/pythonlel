def display_triangle(height, num_triangles):
    for _ in range(num_triangles):
        for i in range(1, height + 1):
            print('*' * i)
        print()

# Example usage
display_triangle(5, 3)
