"""Service module 38496: business logic, no crypto."""


def calculate_total_38496(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38496():
    return 'module 38496 handles orders and invoices'
