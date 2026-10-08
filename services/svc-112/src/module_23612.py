"""Service module 23612: business logic, no crypto."""


def calculate_total_23612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23612():
    return 'module 23612 handles orders and invoices'
