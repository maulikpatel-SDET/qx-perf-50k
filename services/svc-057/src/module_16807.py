"""Service module 16807: business logic, no crypto."""


def calculate_total_16807(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16807():
    return 'module 16807 handles orders and invoices'
