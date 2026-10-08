"""Service module 24336: business logic, no crypto."""


def calculate_total_24336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24336():
    return 'module 24336 handles orders and invoices'
