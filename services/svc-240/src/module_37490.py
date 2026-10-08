"""Service module 37490: business logic, no crypto."""


def calculate_total_37490(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37490():
    return 'module 37490 handles orders and invoices'
