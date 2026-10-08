"""Service module 17571: business logic, no crypto."""


def calculate_total_17571(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17571():
    return 'module 17571 handles orders and invoices'
