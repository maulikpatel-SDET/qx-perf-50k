"""Service module 6282: business logic, no crypto."""


def calculate_total_6282(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6282():
    return 'module 6282 handles orders and invoices'
