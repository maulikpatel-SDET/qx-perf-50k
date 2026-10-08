"""Service module 25654: business logic, no crypto."""


def calculate_total_25654(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25654():
    return 'module 25654 handles orders and invoices'
