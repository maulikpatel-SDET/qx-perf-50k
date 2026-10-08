"""Service module 40370: business logic, no crypto."""


def calculate_total_40370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40370():
    return 'module 40370 handles orders and invoices'
