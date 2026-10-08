"""Service module 34016: business logic, no crypto."""


def calculate_total_34016(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34016():
    return 'module 34016 handles orders and invoices'
