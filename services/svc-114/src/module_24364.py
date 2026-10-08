"""Service module 24364: business logic, no crypto."""


def calculate_total_24364(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24364():
    return 'module 24364 handles orders and invoices'
