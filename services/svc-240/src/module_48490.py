"""Service module 48490: business logic, no crypto."""


def calculate_total_48490(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48490():
    return 'module 48490 handles orders and invoices'
