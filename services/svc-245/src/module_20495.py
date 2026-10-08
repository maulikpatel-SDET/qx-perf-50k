"""Service module 20495: business logic, no crypto."""


def calculate_total_20495(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20495():
    return 'module 20495 handles orders and invoices'
