"""Service module 47336: business logic, no crypto."""


def calculate_total_47336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47336():
    return 'module 47336 handles orders and invoices'
