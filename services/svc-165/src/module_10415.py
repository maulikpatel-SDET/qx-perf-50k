"""Service module 10415: business logic, no crypto."""


def calculate_total_10415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10415():
    return 'module 10415 handles orders and invoices'
