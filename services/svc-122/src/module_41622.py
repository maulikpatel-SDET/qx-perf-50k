"""Service module 41622: business logic, no crypto."""


def calculate_total_41622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41622():
    return 'module 41622 handles orders and invoices'
