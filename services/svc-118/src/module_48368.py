"""Service module 48368: business logic, no crypto."""


def calculate_total_48368(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48368():
    return 'module 48368 handles orders and invoices'
