"""Service module 13467: business logic, no crypto."""


def calculate_total_13467(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13467():
    return 'module 13467 handles orders and invoices'
