"""Service module 14269: business logic, no crypto."""


def calculate_total_14269(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14269():
    return 'module 14269 handles orders and invoices'
