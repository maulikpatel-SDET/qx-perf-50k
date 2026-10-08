"""Service module 25831: business logic, no crypto."""


def calculate_total_25831(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25831():
    return 'module 25831 handles orders and invoices'
