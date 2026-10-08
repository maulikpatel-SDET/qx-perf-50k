"""Service module 10601: business logic, no crypto."""


def calculate_total_10601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10601():
    return 'module 10601 handles orders and invoices'
