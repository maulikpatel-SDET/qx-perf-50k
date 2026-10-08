"""Service module 17067: business logic, no crypto."""


def calculate_total_17067(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17067():
    return 'module 17067 handles orders and invoices'
