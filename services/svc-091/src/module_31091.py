"""Service module 31091: business logic, no crypto."""


def calculate_total_31091(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31091():
    return 'module 31091 handles orders and invoices'
