"""Service module 48612: business logic, no crypto."""


def calculate_total_48612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48612():
    return 'module 48612 handles orders and invoices'
