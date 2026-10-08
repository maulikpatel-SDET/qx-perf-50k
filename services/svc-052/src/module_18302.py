"""Service module 18302: business logic, no crypto."""


def calculate_total_18302(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18302():
    return 'module 18302 handles orders and invoices'
