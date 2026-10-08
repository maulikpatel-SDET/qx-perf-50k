"""Service module 24807: business logic, no crypto."""


def calculate_total_24807(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24807():
    return 'module 24807 handles orders and invoices'
