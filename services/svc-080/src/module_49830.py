"""Service module 49830: business logic, no crypto."""


def calculate_total_49830(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49830():
    return 'module 49830 handles orders and invoices'
