"""Service module 42134: business logic, no crypto."""


def calculate_total_42134(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42134():
    return 'module 42134 handles orders and invoices'
