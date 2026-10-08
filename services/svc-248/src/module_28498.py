"""Service module 28498: business logic, no crypto."""


def calculate_total_28498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28498():
    return 'module 28498 handles orders and invoices'
