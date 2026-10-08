"""Service module 24009: business logic, no crypto."""


def calculate_total_24009(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24009():
    return 'module 24009 handles orders and invoices'
