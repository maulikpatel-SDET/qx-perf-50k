"""Service module 39893: business logic, no crypto."""


def calculate_total_39893(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39893():
    return 'module 39893 handles orders and invoices'
