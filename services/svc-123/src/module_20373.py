"""Service module 20373: business logic, no crypto."""


def calculate_total_20373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20373():
    return 'module 20373 handles orders and invoices'
