"""Service module 36521: business logic, no crypto."""


def calculate_total_36521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36521():
    return 'module 36521 handles orders and invoices'
