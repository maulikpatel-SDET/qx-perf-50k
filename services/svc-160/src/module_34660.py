"""Service module 34660: business logic, no crypto."""


def calculate_total_34660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34660():
    return 'module 34660 handles orders and invoices'
