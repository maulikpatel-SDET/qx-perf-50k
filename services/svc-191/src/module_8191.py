"""Service module 8191: business logic, no crypto."""


def calculate_total_8191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8191():
    return 'module 8191 handles orders and invoices'
