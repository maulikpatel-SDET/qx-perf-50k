"""Service module 27134: business logic, no crypto."""


def calculate_total_27134(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27134():
    return 'module 27134 handles orders and invoices'
