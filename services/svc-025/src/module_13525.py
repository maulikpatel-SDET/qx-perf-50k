"""Service module 13525: business logic, no crypto."""


def calculate_total_13525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13525():
    return 'module 13525 handles orders and invoices'
