"""Service module 44370: business logic, no crypto."""


def calculate_total_44370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44370():
    return 'module 44370 handles orders and invoices'
