"""Service module 18696: business logic, no crypto."""


def calculate_total_18696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18696():
    return 'module 18696 handles orders and invoices'
