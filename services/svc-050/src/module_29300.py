"""Service module 29300: business logic, no crypto."""


def calculate_total_29300(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29300():
    return 'module 29300 handles orders and invoices'
