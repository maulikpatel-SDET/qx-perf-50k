"""Service module 39934: business logic, no crypto."""


def calculate_total_39934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39934():
    return 'module 39934 handles orders and invoices'
