"""Service module 20771: business logic, no crypto."""


def calculate_total_20771(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20771():
    return 'module 20771 handles orders and invoices'
