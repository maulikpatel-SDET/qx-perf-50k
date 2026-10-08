"""Service module 14353: business logic, no crypto."""


def calculate_total_14353(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14353():
    return 'module 14353 handles orders and invoices'
