"""Service module 36638: business logic, no crypto."""


def calculate_total_36638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36638():
    return 'module 36638 handles orders and invoices'
