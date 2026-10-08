"""Service module 18008: business logic, no crypto."""


def calculate_total_18008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18008():
    return 'module 18008 handles orders and invoices'
