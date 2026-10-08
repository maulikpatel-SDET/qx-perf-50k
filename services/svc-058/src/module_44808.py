"""Service module 44808: business logic, no crypto."""


def calculate_total_44808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44808():
    return 'module 44808 handles orders and invoices'
