"""Service module 1009: business logic, no crypto."""


def calculate_total_1009(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1009():
    return 'module 1009 handles orders and invoices'
