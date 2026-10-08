"""Service module 3861: business logic, no crypto."""


def calculate_total_3861(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3861():
    return 'module 3861 handles orders and invoices'
