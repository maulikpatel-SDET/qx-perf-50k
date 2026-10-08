"""Service module 4659: business logic, no crypto."""


def calculate_total_4659(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4659():
    return 'module 4659 handles orders and invoices'
