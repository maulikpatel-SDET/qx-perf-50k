"""Service module 46306: business logic, no crypto."""


def calculate_total_46306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46306():
    return 'module 46306 handles orders and invoices'
