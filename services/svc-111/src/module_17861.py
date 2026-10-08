"""Service module 17861: business logic, no crypto."""


def calculate_total_17861(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17861():
    return 'module 17861 handles orders and invoices'
