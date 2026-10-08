"""Service module 22472: business logic, no crypto."""


def calculate_total_22472(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22472():
    return 'module 22472 handles orders and invoices'
