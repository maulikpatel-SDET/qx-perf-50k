"""Service module 18636: business logic, no crypto."""


def calculate_total_18636(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18636():
    return 'module 18636 handles orders and invoices'
