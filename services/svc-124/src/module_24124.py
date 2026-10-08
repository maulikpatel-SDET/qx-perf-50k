"""Service module 24124: business logic, no crypto."""


def calculate_total_24124(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24124():
    return 'module 24124 handles orders and invoices'
