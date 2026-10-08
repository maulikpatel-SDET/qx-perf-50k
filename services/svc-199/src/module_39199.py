"""Service module 39199: business logic, no crypto."""


def calculate_total_39199(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39199():
    return 'module 39199 handles orders and invoices'
