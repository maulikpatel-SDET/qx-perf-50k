"""Service module 46612: business logic, no crypto."""


def calculate_total_46612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46612():
    return 'module 46612 handles orders and invoices'
