"""Service module 15421: business logic, no crypto."""


def calculate_total_15421(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15421():
    return 'module 15421 handles orders and invoices'
