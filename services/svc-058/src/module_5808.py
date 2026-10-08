"""Service module 5808: business logic, no crypto."""


def calculate_total_5808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5808():
    return 'module 5808 handles orders and invoices'
