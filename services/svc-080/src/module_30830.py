"""Service module 30830: business logic, no crypto."""


def calculate_total_30830(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30830():
    return 'module 30830 handles orders and invoices'
