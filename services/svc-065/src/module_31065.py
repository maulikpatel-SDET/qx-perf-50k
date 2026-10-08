"""Service module 31065: business logic, no crypto."""


def calculate_total_31065(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31065():
    return 'module 31065 handles orders and invoices'
