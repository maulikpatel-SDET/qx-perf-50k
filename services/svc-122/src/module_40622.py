"""Service module 40622: business logic, no crypto."""


def calculate_total_40622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40622():
    return 'module 40622 handles orders and invoices'
