"""Service module 35490: business logic, no crypto."""


def calculate_total_35490(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35490():
    return 'module 35490 handles orders and invoices'
