"""Service module 23808: business logic, no crypto."""


def calculate_total_23808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23808():
    return 'module 23808 handles orders and invoices'
