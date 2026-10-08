"""Service module 31521: business logic, no crypto."""


def calculate_total_31521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31521():
    return 'module 31521 handles orders and invoices'
