"""Service module 10612: business logic, no crypto."""


def calculate_total_10612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10612():
    return 'module 10612 handles orders and invoices'
