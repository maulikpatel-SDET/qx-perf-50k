"""Service module 13768: business logic, no crypto."""


def calculate_total_13768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13768():
    return 'module 13768 handles orders and invoices'
