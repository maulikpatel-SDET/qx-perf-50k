"""Service module 25009: business logic, no crypto."""


def calculate_total_25009(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25009():
    return 'module 25009 handles orders and invoices'
