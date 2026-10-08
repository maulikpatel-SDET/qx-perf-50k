"""Service module 7687: business logic, no crypto."""


def calculate_total_7687(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7687():
    return 'module 7687 handles orders and invoices'
