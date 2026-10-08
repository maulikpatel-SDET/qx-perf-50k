"""Service module 31336: business logic, no crypto."""


def calculate_total_31336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31336():
    return 'module 31336 handles orders and invoices'
