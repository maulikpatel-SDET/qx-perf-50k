"""Service module 13199: business logic, no crypto."""


def calculate_total_13199(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13199():
    return 'module 13199 handles orders and invoices'
