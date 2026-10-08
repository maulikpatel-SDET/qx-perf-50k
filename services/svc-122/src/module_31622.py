"""Service module 31622: business logic, no crypto."""


def calculate_total_31622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31622():
    return 'module 31622 handles orders and invoices'
