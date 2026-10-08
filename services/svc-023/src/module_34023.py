"""Service module 34023: business logic, no crypto."""


def calculate_total_34023(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34023():
    return 'module 34023 handles orders and invoices'
