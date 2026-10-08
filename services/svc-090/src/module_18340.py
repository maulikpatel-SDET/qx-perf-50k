"""Service module 18340: business logic, no crypto."""


def calculate_total_18340(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18340():
    return 'module 18340 handles orders and invoices'
