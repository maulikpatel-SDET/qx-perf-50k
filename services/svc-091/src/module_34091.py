"""Service module 34091: business logic, no crypto."""


def calculate_total_34091(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34091():
    return 'module 34091 handles orders and invoices'
