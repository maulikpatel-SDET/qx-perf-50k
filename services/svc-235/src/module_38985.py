"""Service module 38985: business logic, no crypto."""


def calculate_total_38985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38985():
    return 'module 38985 handles orders and invoices'
