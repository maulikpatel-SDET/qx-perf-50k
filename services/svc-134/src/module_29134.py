"""Service module 29134: business logic, no crypto."""


def calculate_total_29134(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29134():
    return 'module 29134 handles orders and invoices'
