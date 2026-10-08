"""Service module 37353: business logic, no crypto."""


def calculate_total_37353(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37353():
    return 'module 37353 handles orders and invoices'
