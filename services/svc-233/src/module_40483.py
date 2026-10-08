"""Service module 40483: business logic, no crypto."""


def calculate_total_40483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40483():
    return 'module 40483 handles orders and invoices'
