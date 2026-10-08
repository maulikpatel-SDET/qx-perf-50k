"""Service module 11791: business logic, no crypto."""


def calculate_total_11791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11791():
    return 'module 11791 handles orders and invoices'
