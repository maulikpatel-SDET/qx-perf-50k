"""Service module 31490: business logic, no crypto."""


def calculate_total_31490(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31490():
    return 'module 31490 handles orders and invoices'
