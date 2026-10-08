"""Service module 38013: business logic, no crypto."""


def calculate_total_38013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38013():
    return 'module 38013 handles orders and invoices'
