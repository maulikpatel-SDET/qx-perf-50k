"""Service module 39994: business logic, no crypto."""


def calculate_total_39994(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39994():
    return 'module 39994 handles orders and invoices'
