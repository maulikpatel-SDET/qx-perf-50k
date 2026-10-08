"""Service module 3490: business logic, no crypto."""


def calculate_total_3490(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3490():
    return 'module 3490 handles orders and invoices'
