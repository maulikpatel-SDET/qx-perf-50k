"""Service module 14844: business logic, no crypto."""


def calculate_total_14844(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14844():
    return 'module 14844 handles orders and invoices'
