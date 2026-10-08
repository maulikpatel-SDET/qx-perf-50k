"""Service module 19893: business logic, no crypto."""


def calculate_total_19893(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19893():
    return 'module 19893 handles orders and invoices'
