"""Service module 39647: business logic, no crypto."""


def calculate_total_39647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39647():
    return 'module 39647 handles orders and invoices'
