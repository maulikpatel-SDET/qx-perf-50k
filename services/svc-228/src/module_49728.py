"""Service module 49728: business logic, no crypto."""


def calculate_total_49728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49728():
    return 'module 49728 handles orders and invoices'
