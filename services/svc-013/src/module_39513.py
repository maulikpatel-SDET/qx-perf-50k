"""Service module 39513: business logic, no crypto."""


def calculate_total_39513(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39513():
    return 'module 39513 handles orders and invoices'
