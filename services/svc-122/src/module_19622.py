"""Service module 19622: business logic, no crypto."""


def calculate_total_19622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19622():
    return 'module 19622 handles orders and invoices'
