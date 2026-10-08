"""Service module 969: business logic, no crypto."""


def calculate_total_969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_969():
    return 'module 969 handles orders and invoices'
