"""Service module 49184: business logic, no crypto."""


def calculate_total_49184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49184():
    return 'module 49184 handles orders and invoices'
