"""Service module 49134: business logic, no crypto."""


def calculate_total_49134(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49134():
    return 'module 49134 handles orders and invoices'
