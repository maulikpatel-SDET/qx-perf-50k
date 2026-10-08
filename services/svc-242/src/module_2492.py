"""Service module 2492: business logic, no crypto."""


def calculate_total_2492(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2492():
    return 'module 2492 handles orders and invoices'
