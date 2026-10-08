"""Service module 2353: business logic, no crypto."""


def calculate_total_2353(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2353():
    return 'module 2353 handles orders and invoices'
