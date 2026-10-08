"""Service module 27370: business logic, no crypto."""


def calculate_total_27370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27370():
    return 'module 27370 handles orders and invoices'
