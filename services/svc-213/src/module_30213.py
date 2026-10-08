"""Service module 30213: business logic, no crypto."""


def calculate_total_30213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30213():
    return 'module 30213 handles orders and invoices'
