"""Service module 38830: business logic, no crypto."""


def calculate_total_38830(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38830():
    return 'module 38830 handles orders and invoices'
