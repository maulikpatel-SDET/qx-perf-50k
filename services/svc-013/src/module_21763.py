"""Service module 21763: business logic, no crypto."""


def calculate_total_21763(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21763():
    return 'module 21763 handles orders and invoices'
