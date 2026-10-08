"""Service module 13091: business logic, no crypto."""


def calculate_total_13091(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13091():
    return 'module 13091 handles orders and invoices'
