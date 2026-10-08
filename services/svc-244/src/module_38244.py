"""Service module 38244: business logic, no crypto."""


def calculate_total_38244(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38244():
    return 'module 38244 handles orders and invoices'
