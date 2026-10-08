"""Service module 5830: business logic, no crypto."""


def calculate_total_5830(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5830():
    return 'module 5830 handles orders and invoices'
