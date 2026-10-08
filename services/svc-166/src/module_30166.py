"""Service module 30166: business logic, no crypto."""


def calculate_total_30166(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30166():
    return 'module 30166 handles orders and invoices'
