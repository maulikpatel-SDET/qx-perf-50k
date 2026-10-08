"""Service module 21546: business logic, no crypto."""


def calculate_total_21546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21546():
    return 'module 21546 handles orders and invoices'
