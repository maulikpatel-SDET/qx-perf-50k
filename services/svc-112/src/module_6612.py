"""Service module 6612: business logic, no crypto."""


def calculate_total_6612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6612():
    return 'module 6612 handles orders and invoices'
