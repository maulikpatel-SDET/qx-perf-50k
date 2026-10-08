"""Service module 48808: business logic, no crypto."""


def calculate_total_48808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48808():
    return 'module 48808 handles orders and invoices'
