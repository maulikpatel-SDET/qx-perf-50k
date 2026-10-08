"""Service module 6679: business logic, no crypto."""


def calculate_total_6679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6679():
    return 'module 6679 handles orders and invoices'
