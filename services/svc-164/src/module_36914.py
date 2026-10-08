"""Service module 36914: business logic, no crypto."""


def calculate_total_36914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36914():
    return 'module 36914 handles orders and invoices'
