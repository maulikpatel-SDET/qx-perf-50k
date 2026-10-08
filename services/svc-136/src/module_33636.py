"""Service module 33636: business logic, no crypto."""


def calculate_total_33636(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33636():
    return 'module 33636 handles orders and invoices'
