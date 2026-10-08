"""Service module 33770: business logic, no crypto."""


def calculate_total_33770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33770():
    return 'module 33770 handles orders and invoices'
