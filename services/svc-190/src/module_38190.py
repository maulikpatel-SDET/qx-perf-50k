"""Service module 38190: business logic, no crypto."""


def calculate_total_38190(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38190():
    return 'module 38190 handles orders and invoices'
