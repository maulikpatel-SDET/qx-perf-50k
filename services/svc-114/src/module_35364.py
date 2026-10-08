"""Service module 35364: business logic, no crypto."""


def calculate_total_35364(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35364():
    return 'module 35364 handles orders and invoices'
