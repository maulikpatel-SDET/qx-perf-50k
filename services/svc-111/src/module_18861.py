"""Service module 18861: business logic, no crypto."""


def calculate_total_18861(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18861():
    return 'module 18861 handles orders and invoices'
