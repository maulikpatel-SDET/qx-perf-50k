"""Service module 40950: business logic, no crypto."""


def calculate_total_40950(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40950():
    return 'module 40950 handles orders and invoices'
