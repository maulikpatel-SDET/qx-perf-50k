"""Service module 30364: business logic, no crypto."""


def calculate_total_30364(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30364():
    return 'module 30364 handles orders and invoices'
