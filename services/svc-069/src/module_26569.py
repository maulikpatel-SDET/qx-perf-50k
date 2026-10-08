"""Service module 26569: business logic, no crypto."""


def calculate_total_26569(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26569():
    return 'module 26569 handles orders and invoices'
