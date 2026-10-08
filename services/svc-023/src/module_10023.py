"""Service module 10023: business logic, no crypto."""


def calculate_total_10023(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10023():
    return 'module 10023 handles orders and invoices'
