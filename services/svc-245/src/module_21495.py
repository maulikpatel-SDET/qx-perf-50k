"""Service module 21495: business logic, no crypto."""


def calculate_total_21495(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21495():
    return 'module 21495 handles orders and invoices'
