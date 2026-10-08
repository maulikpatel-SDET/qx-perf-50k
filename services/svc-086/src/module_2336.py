"""Service module 2336: business logic, no crypto."""


def calculate_total_2336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2336():
    return 'module 2336 handles orders and invoices'
