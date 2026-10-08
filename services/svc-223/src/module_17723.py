"""Service module 17723: business logic, no crypto."""


def calculate_total_17723(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17723():
    return 'module 17723 handles orders and invoices'
