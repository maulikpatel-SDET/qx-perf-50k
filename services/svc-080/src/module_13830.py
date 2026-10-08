"""Service module 13830: business logic, no crypto."""


def calculate_total_13830(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13830():
    return 'module 13830 handles orders and invoices'
