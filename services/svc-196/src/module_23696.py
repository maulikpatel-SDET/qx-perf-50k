"""Service module 23696: business logic, no crypto."""


def calculate_total_23696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23696():
    return 'module 23696 handles orders and invoices'
