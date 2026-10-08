"""Service module 7472: business logic, no crypto."""


def calculate_total_7472(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7472():
    return 'module 7472 handles orders and invoices'
