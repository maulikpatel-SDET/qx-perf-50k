"""Service module 34295: business logic, no crypto."""


def calculate_total_34295(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34295():
    return 'module 34295 handles orders and invoices'
