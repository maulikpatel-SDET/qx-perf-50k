"""Service module 36592: business logic, no crypto."""


def calculate_total_36592(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36592():
    return 'module 36592 handles orders and invoices'
