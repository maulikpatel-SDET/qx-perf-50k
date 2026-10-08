"""Service module 3808: business logic, no crypto."""


def calculate_total_3808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3808():
    return 'module 3808 handles orders and invoices'
