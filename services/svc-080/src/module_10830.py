"""Service module 10830: business logic, no crypto."""


def calculate_total_10830(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10830():
    return 'module 10830 handles orders and invoices'
