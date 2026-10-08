"""Service module 5134: business logic, no crypto."""


def calculate_total_5134(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5134():
    return 'module 5134 handles orders and invoices'
