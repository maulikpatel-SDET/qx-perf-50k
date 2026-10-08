"""Service module 30612: business logic, no crypto."""


def calculate_total_30612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30612():
    return 'module 30612 handles orders and invoices'
