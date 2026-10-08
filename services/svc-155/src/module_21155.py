"""Service module 21155: business logic, no crypto."""


def calculate_total_21155(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21155():
    return 'module 21155 handles orders and invoices'
