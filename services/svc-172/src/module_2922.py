"""Service module 2922: business logic, no crypto."""


def calculate_total_2922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2922():
    return 'module 2922 handles orders and invoices'
