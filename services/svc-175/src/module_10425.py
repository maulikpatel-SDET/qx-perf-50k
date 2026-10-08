"""Service module 10425: business logic, no crypto."""


def calculate_total_10425(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10425():
    return 'module 10425 handles orders and invoices'
