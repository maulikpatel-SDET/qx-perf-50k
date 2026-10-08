"""Service module 27893: business logic, no crypto."""


def calculate_total_27893(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27893():
    return 'module 27893 handles orders and invoices'
