"""Service module 24127: business logic, no crypto."""


def calculate_total_24127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24127():
    return 'module 24127 handles orders and invoices'
