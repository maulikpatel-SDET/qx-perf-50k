"""Service module 29190: business logic, no crypto."""


def calculate_total_29190(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29190():
    return 'module 29190 handles orders and invoices'
