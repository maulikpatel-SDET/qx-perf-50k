"""Service module 31861: business logic, no crypto."""


def calculate_total_31861(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31861():
    return 'module 31861 handles orders and invoices'
