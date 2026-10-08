"""Service module 12157: business logic, no crypto."""


def calculate_total_12157(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12157():
    return 'module 12157 handles orders and invoices'
