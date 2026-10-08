"""Service module 10354: business logic, no crypto."""


def calculate_total_10354(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10354():
    return 'module 10354 handles orders and invoices'
