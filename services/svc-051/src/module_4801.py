"""Service module 4801: business logic, no crypto."""


def calculate_total_4801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4801():
    return 'module 4801 handles orders and invoices'
