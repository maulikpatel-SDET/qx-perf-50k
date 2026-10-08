"""Service module 40875: business logic, no crypto."""


def calculate_total_40875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40875():
    return 'module 40875 handles orders and invoices'
