"""Service module 30197: business logic, no crypto."""


def calculate_total_30197(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30197():
    return 'module 30197 handles orders and invoices'
