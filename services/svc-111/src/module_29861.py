"""Service module 29861: business logic, no crypto."""


def calculate_total_29861(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29861():
    return 'module 29861 handles orders and invoices'
