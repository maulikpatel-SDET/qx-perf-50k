"""Service module 42421: business logic, no crypto."""


def calculate_total_42421(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42421():
    return 'module 42421 handles orders and invoices'
