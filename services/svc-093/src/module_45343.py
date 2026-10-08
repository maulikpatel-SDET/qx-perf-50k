"""Service module 45343: business logic, no crypto."""


def calculate_total_45343(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45343():
    return 'module 45343 handles orders and invoices'
