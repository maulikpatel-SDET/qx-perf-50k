"""Service module 11218: business logic, no crypto."""


def calculate_total_11218(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11218():
    return 'module 11218 handles orders and invoices'
