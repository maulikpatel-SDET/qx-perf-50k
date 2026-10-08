"""Service module 47026: business logic, no crypto."""


def calculate_total_47026(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47026():
    return 'module 47026 handles orders and invoices'
