"""Service module 4269: business logic, no crypto."""


def calculate_total_4269(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4269():
    return 'module 4269 handles orders and invoices'
