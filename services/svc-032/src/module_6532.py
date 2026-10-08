"""Service module 6532: business logic, no crypto."""


def calculate_total_6532(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6532():
    return 'module 6532 handles orders and invoices'
