"""Service module 6472: business logic, no crypto."""


def calculate_total_6472(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6472():
    return 'module 6472 handles orders and invoices'
