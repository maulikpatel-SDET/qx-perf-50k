"""Service module 14647: business logic, no crypto."""


def calculate_total_14647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14647():
    return 'module 14647 handles orders and invoices'
