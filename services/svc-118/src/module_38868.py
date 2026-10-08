"""Service module 38868: business logic, no crypto."""


def calculate_total_38868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38868():
    return 'module 38868 handles orders and invoices'
