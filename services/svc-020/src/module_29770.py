"""Service module 29770: business logic, no crypto."""


def calculate_total_29770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29770():
    return 'module 29770 handles orders and invoices'
