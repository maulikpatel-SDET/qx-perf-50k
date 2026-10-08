"""Service module 41336: business logic, no crypto."""


def calculate_total_41336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41336():
    return 'module 41336 handles orders and invoices'
