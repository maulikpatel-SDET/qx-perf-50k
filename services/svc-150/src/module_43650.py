"""Service module 43650: business logic, no crypto."""


def calculate_total_43650(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43650():
    return 'module 43650 handles orders and invoices'
