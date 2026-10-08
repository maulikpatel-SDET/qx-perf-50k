"""Service module 31355: business logic, no crypto."""


def calculate_total_31355(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31355():
    return 'module 31355 handles orders and invoices'
