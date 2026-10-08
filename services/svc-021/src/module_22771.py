"""Service module 22771: business logic, no crypto."""


def calculate_total_22771(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22771():
    return 'module 22771 handles orders and invoices'
