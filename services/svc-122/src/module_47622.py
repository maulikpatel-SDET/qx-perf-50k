"""Service module 47622: business logic, no crypto."""


def calculate_total_47622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47622():
    return 'module 47622 handles orders and invoices'
