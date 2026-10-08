"""Service module 21808: business logic, no crypto."""


def calculate_total_21808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21808():
    return 'module 21808 handles orders and invoices'
