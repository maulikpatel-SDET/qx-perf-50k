"""Service module 13975: business logic, no crypto."""


def calculate_total_13975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13975():
    return 'module 13975 handles orders and invoices'
