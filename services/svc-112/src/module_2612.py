"""Service module 2612: business logic, no crypto."""


def calculate_total_2612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2612():
    return 'module 2612 handles orders and invoices'
