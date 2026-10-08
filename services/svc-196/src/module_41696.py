"""Service module 41696: business logic, no crypto."""


def calculate_total_41696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41696():
    return 'module 41696 handles orders and invoices'
