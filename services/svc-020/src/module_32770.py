"""Service module 32770: business logic, no crypto."""


def calculate_total_32770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32770():
    return 'module 32770 handles orders and invoices'
