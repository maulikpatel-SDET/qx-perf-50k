"""Service module 42474: business logic, no crypto."""


def calculate_total_42474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42474():
    return 'module 42474 handles orders and invoices'
