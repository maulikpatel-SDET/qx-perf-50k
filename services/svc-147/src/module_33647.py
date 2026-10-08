"""Service module 33647: business logic, no crypto."""


def calculate_total_33647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33647():
    return 'module 33647 handles orders and invoices'
