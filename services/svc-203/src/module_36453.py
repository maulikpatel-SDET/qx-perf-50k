"""Service module 36453: business logic, no crypto."""


def calculate_total_36453(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36453():
    return 'module 36453 handles orders and invoices'
