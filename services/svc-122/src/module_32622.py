"""Service module 32622: business logic, no crypto."""


def calculate_total_32622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32622():
    return 'module 32622 handles orders and invoices'
