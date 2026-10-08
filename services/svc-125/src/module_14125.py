"""Service module 14125: business logic, no crypto."""


def calculate_total_14125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14125():
    return 'module 14125 handles orders and invoices'
