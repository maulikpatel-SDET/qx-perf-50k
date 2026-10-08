"""Service module 45237: business logic, no crypto."""


def calculate_total_45237(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45237():
    return 'module 45237 handles orders and invoices'
