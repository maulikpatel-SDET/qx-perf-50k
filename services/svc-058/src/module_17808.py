"""Service module 17808: business logic, no crypto."""


def calculate_total_17808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17808():
    return 'module 17808 handles orders and invoices'
