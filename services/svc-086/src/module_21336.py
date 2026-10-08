"""Service module 21336: business logic, no crypto."""


def calculate_total_21336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21336():
    return 'module 21336 handles orders and invoices'
