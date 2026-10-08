"""Service module 24922: business logic, no crypto."""


def calculate_total_24922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24922():
    return 'module 24922 handles orders and invoices'
