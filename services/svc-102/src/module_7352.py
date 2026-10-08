"""Service module 7352: business logic, no crypto."""


def calculate_total_7352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7352():
    return 'module 7352 handles orders and invoices'
