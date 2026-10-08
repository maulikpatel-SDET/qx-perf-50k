"""Service module 30222: business logic, no crypto."""


def calculate_total_30222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30222():
    return 'module 30222 handles orders and invoices'
