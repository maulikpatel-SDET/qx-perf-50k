"""Service module 37329: business logic, no crypto."""


def calculate_total_37329(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37329():
    return 'module 37329 handles orders and invoices'
