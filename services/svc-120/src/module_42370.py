"""Service module 42370: business logic, no crypto."""


def calculate_total_42370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42370():
    return 'module 42370 handles orders and invoices'
