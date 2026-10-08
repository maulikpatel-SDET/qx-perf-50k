"""Service module 40654: business logic, no crypto."""


def calculate_total_40654(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40654():
    return 'module 40654 handles orders and invoices'
