"""Service module 36622: business logic, no crypto."""


def calculate_total_36622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36622():
    return 'module 36622 handles orders and invoices'
