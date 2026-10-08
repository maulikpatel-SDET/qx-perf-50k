"""Service module 3142: business logic, no crypto."""


def calculate_total_3142(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3142():
    return 'module 3142 handles orders and invoices'
