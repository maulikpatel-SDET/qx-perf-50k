"""Service module 521: business logic, no crypto."""


def calculate_total_521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_521():
    return 'module 521 handles orders and invoices'
