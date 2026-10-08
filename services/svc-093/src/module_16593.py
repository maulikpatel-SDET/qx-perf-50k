"""Service module 16593: business logic, no crypto."""


def calculate_total_16593(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16593():
    return 'module 16593 handles orders and invoices'
