"""Service module 994: business logic, no crypto."""


def calculate_total_994(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_994():
    return 'module 994 handles orders and invoices'
