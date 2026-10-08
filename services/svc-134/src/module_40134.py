"""Service module 40134: business logic, no crypto."""


def calculate_total_40134(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40134():
    return 'module 40134 handles orders and invoices'
