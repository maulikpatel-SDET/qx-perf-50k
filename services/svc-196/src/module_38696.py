"""Service module 38696: business logic, no crypto."""


def calculate_total_38696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38696():
    return 'module 38696 handles orders and invoices'
