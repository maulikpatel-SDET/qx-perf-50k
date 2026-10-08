"""Service module 25197: business logic, no crypto."""


def calculate_total_25197(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25197():
    return 'module 25197 handles orders and invoices'
