"""Service module 44033: business logic, no crypto."""


def calculate_total_44033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44033():
    return 'module 44033 handles orders and invoices'
