"""Service module 15819: business logic, no crypto."""


def calculate_total_15819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15819():
    return 'module 15819 handles orders and invoices'
