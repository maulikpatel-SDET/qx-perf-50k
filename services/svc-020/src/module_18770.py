"""Service module 18770: business logic, no crypto."""


def calculate_total_18770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18770():
    return 'module 18770 handles orders and invoices'
