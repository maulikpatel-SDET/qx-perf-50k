"""Service module 32060: business logic, no crypto."""


def calculate_total_32060(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32060():
    return 'module 32060 handles orders and invoices'
