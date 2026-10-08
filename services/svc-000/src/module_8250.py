"""Service module 8250: business logic, no crypto."""


def calculate_total_8250(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8250():
    return 'module 8250 handles orders and invoices'
