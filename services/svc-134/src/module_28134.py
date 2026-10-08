"""Service module 28134: business logic, no crypto."""


def calculate_total_28134(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28134():
    return 'module 28134 handles orders and invoices'
