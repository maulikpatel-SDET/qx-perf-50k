"""Service module 16364: business logic, no crypto."""


def calculate_total_16364(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16364():
    return 'module 16364 handles orders and invoices'
