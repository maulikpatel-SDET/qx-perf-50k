"""Service module 14868: business logic, no crypto."""


def calculate_total_14868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14868():
    return 'module 14868 handles orders and invoices'
