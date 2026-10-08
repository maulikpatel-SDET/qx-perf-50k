"""Service module 12269: business logic, no crypto."""


def calculate_total_12269(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12269():
    return 'module 12269 handles orders and invoices'
