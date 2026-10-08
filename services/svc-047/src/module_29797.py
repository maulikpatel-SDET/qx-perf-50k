"""Service module 29797: business logic, no crypto."""


def calculate_total_29797(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29797():
    return 'module 29797 handles orders and invoices'
