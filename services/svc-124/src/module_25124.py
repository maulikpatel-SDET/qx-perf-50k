"""Service module 25124: business logic, no crypto."""


def calculate_total_25124(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25124():
    return 'module 25124 handles orders and invoices'
