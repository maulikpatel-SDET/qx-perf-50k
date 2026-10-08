"""Service module 38527: business logic, no crypto."""


def calculate_total_38527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38527():
    return 'module 38527 handles orders and invoices'
