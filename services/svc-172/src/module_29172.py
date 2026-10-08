"""Service module 29172: business logic, no crypto."""


def calculate_total_29172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29172():
    return 'module 29172 handles orders and invoices'
