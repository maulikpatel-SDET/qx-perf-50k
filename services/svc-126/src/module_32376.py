"""Service module 32376: business logic, no crypto."""


def calculate_total_32376(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32376():
    return 'module 32376 handles orders and invoices'
