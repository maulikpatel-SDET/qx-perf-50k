"""Service module 12190: business logic, no crypto."""


def calculate_total_12190(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12190():
    return 'module 12190 handles orders and invoices'
