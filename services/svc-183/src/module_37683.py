"""Service module 37683: business logic, no crypto."""


def calculate_total_37683(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37683():
    return 'module 37683 handles orders and invoices'
