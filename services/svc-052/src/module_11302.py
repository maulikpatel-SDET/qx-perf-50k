"""Service module 11302: business logic, no crypto."""


def calculate_total_11302(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11302():
    return 'module 11302 handles orders and invoices'
