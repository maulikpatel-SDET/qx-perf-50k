"""Service module 1124: business logic, no crypto."""


def calculate_total_1124(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1124():
    return 'module 1124 handles orders and invoices'
