"""Service module 21355: business logic, no crypto."""


def calculate_total_21355(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21355():
    return 'module 21355 handles orders and invoices'
