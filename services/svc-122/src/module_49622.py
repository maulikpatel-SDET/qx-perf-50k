"""Service module 49622: business logic, no crypto."""


def calculate_total_49622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49622():
    return 'module 49622 handles orders and invoices'
