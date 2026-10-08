"""Service module 1336: business logic, no crypto."""


def calculate_total_1336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1336():
    return 'module 1336 handles orders and invoices'
