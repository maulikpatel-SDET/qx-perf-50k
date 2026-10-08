"""Service module 29336: business logic, no crypto."""


def calculate_total_29336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29336():
    return 'module 29336 handles orders and invoices'
