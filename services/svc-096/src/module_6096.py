"""Service module 6096: business logic, no crypto."""


def calculate_total_6096(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6096():
    return 'module 6096 handles orders and invoices'
