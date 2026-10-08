"""Service module 26518: business logic, no crypto."""


def calculate_total_26518(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26518():
    return 'module 26518 handles orders and invoices'
