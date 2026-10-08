"""Service module 34604: business logic, no crypto."""


def calculate_total_34604(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34604():
    return 'module 34604 handles orders and invoices'
