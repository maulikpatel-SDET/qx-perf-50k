"""Service module 25807: business logic, no crypto."""


def calculate_total_25807(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25807():
    return 'module 25807 handles orders and invoices'
