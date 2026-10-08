"""Service module 12808: business logic, no crypto."""


def calculate_total_12808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12808():
    return 'module 12808 handles orders and invoices'
