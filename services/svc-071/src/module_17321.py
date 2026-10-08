"""Service module 17321: business logic, no crypto."""


def calculate_total_17321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17321():
    return 'module 17321 handles orders and invoices'
