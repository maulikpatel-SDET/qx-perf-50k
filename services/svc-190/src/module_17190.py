"""Service module 17190: business logic, no crypto."""


def calculate_total_17190(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17190():
    return 'module 17190 handles orders and invoices'
