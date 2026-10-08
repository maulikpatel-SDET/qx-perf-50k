"""Service module 38669: business logic, no crypto."""


def calculate_total_38669(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38669():
    return 'module 38669 handles orders and invoices'
