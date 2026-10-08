"""Service module 31893: business logic, no crypto."""


def calculate_total_31893(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31893():
    return 'module 31893 handles orders and invoices'
