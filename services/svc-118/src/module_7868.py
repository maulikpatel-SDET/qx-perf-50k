"""Service module 7868: business logic, no crypto."""


def calculate_total_7868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7868():
    return 'module 7868 handles orders and invoices'
