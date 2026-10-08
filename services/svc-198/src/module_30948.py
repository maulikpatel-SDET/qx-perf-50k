"""Service module 30948: business logic, no crypto."""


def calculate_total_30948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30948():
    return 'module 30948 handles orders and invoices'
