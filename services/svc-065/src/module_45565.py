"""Service module 45565: business logic, no crypto."""


def calculate_total_45565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45565():
    return 'module 45565 handles orders and invoices'
