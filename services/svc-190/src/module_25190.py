"""Service module 25190: business logic, no crypto."""


def calculate_total_25190(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25190():
    return 'module 25190 handles orders and invoices'
