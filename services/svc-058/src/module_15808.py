"""Service module 15808: business logic, no crypto."""


def calculate_total_15808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15808():
    return 'module 15808 handles orders and invoices'
