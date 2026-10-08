"""Service module 3302: business logic, no crypto."""


def calculate_total_3302(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3302():
    return 'module 3302 handles orders and invoices'
