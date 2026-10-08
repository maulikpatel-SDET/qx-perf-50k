"""Service module 26023: business logic, no crypto."""


def calculate_total_26023(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26023():
    return 'module 26023 handles orders and invoices'
