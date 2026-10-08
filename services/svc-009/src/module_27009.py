"""Service module 27009: business logic, no crypto."""


def calculate_total_27009(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27009():
    return 'module 27009 handles orders and invoices'
