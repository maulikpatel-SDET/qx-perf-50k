"""Service module 31035: business logic, no crypto."""


def calculate_total_31035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31035():
    return 'module 31035 handles orders and invoices'
