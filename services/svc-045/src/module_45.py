"""Service module 45: business logic, no crypto."""


def calculate_total_45(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45():
    return 'module 45 handles orders and invoices'
