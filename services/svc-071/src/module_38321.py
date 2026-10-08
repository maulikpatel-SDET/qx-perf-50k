"""Service module 38321: business logic, no crypto."""


def calculate_total_38321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38321():
    return 'module 38321 handles orders and invoices'
