"""Service module 10521: business logic, no crypto."""


def calculate_total_10521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10521():
    return 'module 10521 handles orders and invoices'
