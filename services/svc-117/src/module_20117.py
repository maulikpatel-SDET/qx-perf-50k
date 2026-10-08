"""Service module 20117: business logic, no crypto."""


def calculate_total_20117(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20117():
    return 'module 20117 handles orders and invoices'
