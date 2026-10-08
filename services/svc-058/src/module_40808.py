"""Service module 40808: business logic, no crypto."""


def calculate_total_40808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40808():
    return 'module 40808 handles orders and invoices'
