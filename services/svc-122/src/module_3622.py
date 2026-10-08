"""Service module 3622: business logic, no crypto."""


def calculate_total_3622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3622():
    return 'module 3622 handles orders and invoices'
