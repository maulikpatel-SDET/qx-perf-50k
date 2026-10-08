"""Service module 6830: business logic, no crypto."""


def calculate_total_6830(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6830():
    return 'module 6830 handles orders and invoices'
