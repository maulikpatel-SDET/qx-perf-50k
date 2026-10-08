"""Service module 39273: business logic, no crypto."""


def calculate_total_39273(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39273():
    return 'module 39273 handles orders and invoices'
