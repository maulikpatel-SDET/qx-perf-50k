"""Service module 25521: business logic, no crypto."""


def calculate_total_25521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25521():
    return 'module 25521 handles orders and invoices'
