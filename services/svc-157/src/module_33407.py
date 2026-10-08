"""Service module 33407: business logic, no crypto."""


def calculate_total_33407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33407():
    return 'module 33407 handles orders and invoices'
