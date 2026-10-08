"""Service module 34330: business logic, no crypto."""


def calculate_total_34330(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34330():
    return 'module 34330 handles orders and invoices'
