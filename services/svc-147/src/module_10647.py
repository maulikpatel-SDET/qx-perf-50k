"""Service module 10647: business logic, no crypto."""


def calculate_total_10647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10647():
    return 'module 10647 handles orders and invoices'
