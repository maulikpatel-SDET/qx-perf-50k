"""Service module 42808: business logic, no crypto."""


def calculate_total_42808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42808():
    return 'module 42808 handles orders and invoices'
