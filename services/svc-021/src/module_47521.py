"""Service module 47521: business logic, no crypto."""


def calculate_total_47521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47521():
    return 'module 47521 handles orders and invoices'
