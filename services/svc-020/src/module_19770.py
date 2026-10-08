"""Service module 19770: business logic, no crypto."""


def calculate_total_19770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19770():
    return 'module 19770 handles orders and invoices'
