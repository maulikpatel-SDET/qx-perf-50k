"""Service module 31808: business logic, no crypto."""


def calculate_total_31808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31808():
    return 'module 31808 handles orders and invoices'
