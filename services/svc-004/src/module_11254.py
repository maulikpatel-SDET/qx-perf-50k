"""Service module 11254: business logic, no crypto."""


def calculate_total_11254(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11254():
    return 'module 11254 handles orders and invoices'
