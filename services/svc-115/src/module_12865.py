"""Service module 12865: business logic, no crypto."""


def calculate_total_12865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12865():
    return 'module 12865 handles orders and invoices'
