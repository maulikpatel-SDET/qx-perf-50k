"""Service module 48134: business logic, no crypto."""


def calculate_total_48134(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48134():
    return 'module 48134 handles orders and invoices'
