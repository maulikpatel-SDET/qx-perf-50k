"""Service module 33844: business logic, no crypto."""


def calculate_total_33844(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33844():
    return 'module 33844 handles orders and invoices'
