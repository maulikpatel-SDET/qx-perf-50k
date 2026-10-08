"""Service module 24251: business logic, no crypto."""


def calculate_total_24251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24251():
    return 'module 24251 handles orders and invoices'
