"""Service module 37484: business logic, no crypto."""


def calculate_total_37484(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37484():
    return 'module 37484 handles orders and invoices'
