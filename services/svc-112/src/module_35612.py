"""Service module 35612: business logic, no crypto."""


def calculate_total_35612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35612():
    return 'module 35612 handles orders and invoices'
