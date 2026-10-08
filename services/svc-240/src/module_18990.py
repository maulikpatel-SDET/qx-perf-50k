"""Service module 18990: business logic, no crypto."""


def calculate_total_18990(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18990():
    return 'module 18990 handles orders and invoices'
