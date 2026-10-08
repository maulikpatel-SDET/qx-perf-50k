"""Service module 16405: business logic, no crypto."""


def calculate_total_16405(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16405():
    return 'module 16405 handles orders and invoices'
