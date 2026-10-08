"""Service module 30287: business logic, no crypto."""


def calculate_total_30287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30287():
    return 'module 30287 handles orders and invoices'
