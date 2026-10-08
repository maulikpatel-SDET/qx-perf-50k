"""Service module 4622: business logic, no crypto."""


def calculate_total_4622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4622():
    return 'module 4622 handles orders and invoices'
