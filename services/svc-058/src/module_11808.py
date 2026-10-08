"""Service module 11808: business logic, no crypto."""


def calculate_total_11808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11808():
    return 'module 11808 handles orders and invoices'
