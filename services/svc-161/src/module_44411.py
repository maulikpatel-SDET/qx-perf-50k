"""Service module 44411: business logic, no crypto."""


def calculate_total_44411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44411():
    return 'module 44411 handles orders and invoices'
