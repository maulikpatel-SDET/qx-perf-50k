"""Service module 1023: business logic, no crypto."""


def calculate_total_1023(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1023():
    return 'module 1023 handles orders and invoices'
