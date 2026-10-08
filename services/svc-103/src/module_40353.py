"""Service module 40353: business logic, no crypto."""


def calculate_total_40353(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40353():
    return 'module 40353 handles orders and invoices'
