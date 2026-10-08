"""Service module 37133: business logic, no crypto."""


def calculate_total_37133(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37133():
    return 'module 37133 handles orders and invoices'
