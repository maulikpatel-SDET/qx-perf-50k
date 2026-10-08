"""Service module 25808: business logic, no crypto."""


def calculate_total_25808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25808():
    return 'module 25808 handles orders and invoices'
