"""Service module 21565: business logic, no crypto."""


def calculate_total_21565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21565():
    return 'module 21565 handles orders and invoices'
