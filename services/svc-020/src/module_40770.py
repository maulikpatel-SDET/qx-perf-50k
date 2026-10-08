"""Service module 40770: business logic, no crypto."""


def calculate_total_40770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40770():
    return 'module 40770 handles orders and invoices'
