"""Service module 48467: business logic, no crypto."""


def calculate_total_48467(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48467():
    return 'module 48467 handles orders and invoices'
