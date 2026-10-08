"""Service module 40473: business logic, no crypto."""


def calculate_total_40473(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40473():
    return 'module 40473 handles orders and invoices'
