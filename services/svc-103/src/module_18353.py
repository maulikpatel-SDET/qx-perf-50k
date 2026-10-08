"""Service module 18353: business logic, no crypto."""


def calculate_total_18353(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18353():
    return 'module 18353 handles orders and invoices'
