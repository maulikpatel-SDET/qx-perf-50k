"""Service module 20622: business logic, no crypto."""


def calculate_total_20622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20622():
    return 'module 20622 handles orders and invoices'
