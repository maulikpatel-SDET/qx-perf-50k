"""Service module 30788: business logic, no crypto."""


def calculate_total_30788(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30788():
    return 'module 30788 handles orders and invoices'
