"""Service module 38875: business logic, no crypto."""


def calculate_total_38875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38875():
    return 'module 38875 handles orders and invoices'
