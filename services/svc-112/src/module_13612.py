"""Service module 13612: business logic, no crypto."""


def calculate_total_13612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13612():
    return 'module 13612 handles orders and invoices'
