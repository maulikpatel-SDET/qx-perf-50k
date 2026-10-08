"""Service module 22807: business logic, no crypto."""


def calculate_total_22807(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22807():
    return 'module 22807 handles orders and invoices'
