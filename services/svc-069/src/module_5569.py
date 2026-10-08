"""Service module 5569: business logic, no crypto."""


def calculate_total_5569(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5569():
    return 'module 5569 handles orders and invoices'
