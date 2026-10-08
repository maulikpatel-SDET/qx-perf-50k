"""Service module 39565: business logic, no crypto."""


def calculate_total_39565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39565():
    return 'module 39565 handles orders and invoices'
