"""Service module 20612: business logic, no crypto."""


def calculate_total_20612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20612():
    return 'module 20612 handles orders and invoices'
