"""Service module 37622: business logic, no crypto."""


def calculate_total_37622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37622():
    return 'module 37622 handles orders and invoices'
