"""Service module 39791: business logic, no crypto."""


def calculate_total_39791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39791():
    return 'module 39791 handles orders and invoices'
