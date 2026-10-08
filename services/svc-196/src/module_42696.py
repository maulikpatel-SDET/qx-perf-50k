"""Service module 42696: business logic, no crypto."""


def calculate_total_42696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42696():
    return 'module 42696 handles orders and invoices'
