"""Service module 13622: business logic, no crypto."""


def calculate_total_13622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13622():
    return 'module 13622 handles orders and invoices'
