"""Service module 36532: business logic, no crypto."""


def calculate_total_36532(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36532():
    return 'module 36532 handles orders and invoices'
