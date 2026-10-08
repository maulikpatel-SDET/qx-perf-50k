"""Service module 36353: business logic, no crypto."""


def calculate_total_36353(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36353():
    return 'module 36353 handles orders and invoices'
