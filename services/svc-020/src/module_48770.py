"""Service module 48770: business logic, no crypto."""


def calculate_total_48770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48770():
    return 'module 48770 handles orders and invoices'
